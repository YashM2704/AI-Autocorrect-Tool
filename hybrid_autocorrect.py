from textblob_autocorrect import correct_spelling
from bert_autocorrect import bert_autocorrect


def hybrid_autocorrect(text):

    # Step 1: Correct full sentence
    corrected_text = correct_spelling(text)

    original_words = text.lower().split()
    corrected_words = corrected_text.lower().split()

    suspicious_indices = []

    # Identify corrected words
    for i, (original, corrected) in enumerate(
        zip(original_words, corrected_words)
    ):

        if original != corrected:

            suspicious_indices.append(i)

    bert_suggestions = []

    # Generate contextual suggestions
    for index in suspicious_indices:

        temp_words = corrected_words.copy()

        # Mask corrected word
        temp_words[index] = "[MASK]"

        masked_sentence = " ".join(temp_words)

        # Add punctuation
        if not masked_sentence.endswith("."):
            masked_sentence += "."

        predictions = bert_autocorrect(masked_sentence)

        bert_suggestions.append({

            "masked_sentence": masked_sentence,

            "predictions": predictions
        })

    return {

        "original_text": text,

        "textblob_output": corrected_text,

        "bert_suggestions": bert_suggestions
    }