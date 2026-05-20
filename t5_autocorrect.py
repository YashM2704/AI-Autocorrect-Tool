from transformers import (
    T5Tokenizer,
    T5ForConditionalGeneration
)

from semantic_ranker import (
    calculate_semantic_similarity
)

from grammar_scorer import (
    calculate_grammar_score
)

from penalty_engine import (
    calculate_error_penalty
)


# ---------------------------------------------------
# LOAD TOKENIZER
# ---------------------------------------------------

tokenizer = T5Tokenizer.from_pretrained(
    "vennify/t5-base-grammar-correction"
)


# ---------------------------------------------------
# LOAD MODEL
# ---------------------------------------------------

model = T5ForConditionalGeneration.from_pretrained(
    "vennify/t5-base-grammar-correction"
)


# ---------------------------------------------------
# FINAL SCORING FUNCTION
# ---------------------------------------------------

def calculate_final_score(

    similarity,

    grammar_score,

    correction_strength,

    penalty
):

    final_score = (

        (0.35 * similarity)

        +

        (0.35 * grammar_score)

        +

        (0.30 * correction_strength)

        -

        penalty
    )

    return round(final_score, 3)


# ---------------------------------------------------
# MAIN T5 CORRECTION FUNCTION
# ---------------------------------------------------

def t5_correct_text(text):

    # Add grammar prompt
    input_text = f"grammar: {text}"

    # Tokenize input
    input_ids = tokenizer.encode(

        input_text,

        return_tensors="pt"
    )

    # Generate multiple candidates
    outputs = model.generate(

        input_ids,

        max_length=128,

        num_beams=5,

        num_return_sequences=5,

        early_stopping=True
    )

    candidates = []

    # ---------------------------------------------------
    # PROCESS GENERATED CANDIDATES
    # ---------------------------------------------------

    for output in outputs:

        generated_text = tokenizer.decode(

            output,

            skip_special_tokens=True
        )

        # -------------------------------------------
        # SEMANTIC SIMILARITY
        # -------------------------------------------

        similarity = (

            calculate_semantic_similarity(

                text,

                generated_text
            )
        )

        # -------------------------------------------
        # GRAMMAR QUALITY
        # -------------------------------------------

        grammar_score = (

            calculate_grammar_score(

                generated_text
            )
        )

        # -------------------------------------------
        # CORRECTION STRENGTH
        # -------------------------------------------

        correction_strength = (

            1 - similarity
        )

        # -------------------------------------------
        # TYPO / ERROR PENALTY
        # -------------------------------------------

        penalty = (

            calculate_error_penalty(

                generated_text
            )
        )

        # -------------------------------------------
        # FINAL RANKING SCORE
        # -------------------------------------------

        final_score = calculate_final_score(

            similarity,

            grammar_score,

            correction_strength,

            penalty
        )

        # -------------------------------------------
        # STORE CANDIDATE
        # -------------------------------------------

        candidates.append({

            "text": generated_text,

            "similarity": round(
                similarity,
                3
            ),

            "grammar_score": grammar_score,

            "correction_strength": round(
                correction_strength,
                3
            ),

            "penalty": penalty,

            "final_score": final_score
        })

    # ---------------------------------------------------
    # SORT CANDIDATES
    # ---------------------------------------------------

    ranked_candidates = sorted(

        candidates,

        key=lambda x: x["final_score"],

        reverse=True
    )

    # ---------------------------------------------------
    # BEST CANDIDATE
    # ---------------------------------------------------

    best_candidate = ranked_candidates[0]

    return {

        "best_correction":
        best_candidate["text"],

        "all_candidates":
        ranked_candidates
    }# End of file
