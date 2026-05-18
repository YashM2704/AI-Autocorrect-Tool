from candidate_generator import (
    generate_candidates
)


word = input("Enter typo word: ")

candidates = generate_candidates(word)

print("\nCandidate Suggestions:\n")

for candidate in candidates:

    print(

        f"""
Word:
{candidate['word']}

Fuzzy Score:
{candidate['fuzzy_score']}

Phonetic Match:
{candidate['phonetic_match']}

Frequency Score:
{candidate['frequency_score']}

Final Score:
{candidate['final_score']}
"""
    )