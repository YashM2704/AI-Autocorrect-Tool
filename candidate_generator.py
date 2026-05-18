from rapidfuzz import process

from wordfreq import (
    top_n_list,
    zipf_frequency
)

from metaphone import (
    doublemetaphone
)


# ---------------------------------------------------
# LOAD ENGLISH VOCABULARY
# ---------------------------------------------------

raw_words = top_n_list(
    "en",
    50000
)

# Keep meaningful words only
english_words = [

    word for word in raw_words

    if len(word) > 3
]


# ---------------------------------------------------
# PHONETIC SIMILARITY
# ---------------------------------------------------

def phonetic_similarity(word1, word2):

    code1 = doublemetaphone(word1)[0]

    code2 = doublemetaphone(word2)[0]

    return code1 == code2


# ---------------------------------------------------
# FINAL CANDIDATE SCORE
# ---------------------------------------------------

def calculate_candidate_score(

    fuzzy_score,

    phonetic_match,

    frequency_score
):

    phonetic_bonus = 20 if phonetic_match else 0

    final_score = (

        (0.6 * fuzzy_score)

        +

        phonetic_bonus

        +

        (0.4 * frequency_score)
    )

    return round(final_score, 2)


# ---------------------------------------------------
# GENERATE TYPO CANDIDATES
# ---------------------------------------------------

def generate_candidates(word):

    matches = process.extract(

        word,

        english_words,

        limit=20
    )

    candidates = []

    for match in matches:

        candidate_word = match[0]

        fuzzy_score = match[1]

        # Ignore weak matches
        if fuzzy_score > 65:

            phonetic_match = phonetic_similarity(

                word,

                candidate_word
            )

            # Word frequency
            frequency_score = zipf_frequency(

                candidate_word,

                "en"
            )

            # Final ranking
            final_score = calculate_candidate_score(

                fuzzy_score,

                phonetic_match,

                frequency_score
            )

            candidates.append({

                "word": candidate_word,

                "fuzzy_score": round(
                    fuzzy_score,
                    2
                ),

                "phonetic_match":
                phonetic_match,

                "frequency_score":
                round(
                    frequency_score,
                    2
                ),

                "final_score":
                final_score
            })

    # Sort candidates
    ranked_candidates = sorted(

        candidates,

        key=lambda x: x["final_score"],

        reverse=True
    )

    # Return top 5
    return ranked_candidates[:5]