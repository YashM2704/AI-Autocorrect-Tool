from textblob_autocorrect import correct_spelling
from bert_autocorrect import bert_autocorrect
from utils import calculate_similarity
def hybrid_autocorrect(text):
    corrected_text = correct_spelling(text)
    original_words = text.lower().split()
    corrected_words = corrected_text.lower().split()
    suspicious_indices = []
    confidence_scores = []
    # Compare words
    for i, (original, corrected) in enumerate(
        zip(original_words, corrected_words)
    ):
        similarity = calculate_similarity(
            original,
            corrected
        )
        confidence_scores.append({
            "original": original,
            "corrected": corrected,
            "similarity": similarity
        })
        # Lower similarity means more suspicious
        if similarity < 0.7:
            suspicious_indices.append(i)
    bert_suggestions = []
    # Generate contextual suggestions
    for index in suspicious_indices:
        temp_words = corrected_words.copy()
        temp_words[index] = "[MASK]"
        masked_sentence = " ".join(temp_words)
        if not masked_sentence.endswith("."):
            masked_sentence += "."
        predictions = bert_autocorrect(
            masked_sentence
        )
        bert_suggestions.append({
            "masked_sentence": masked_sentence,
            "predictions": predictions
        })
    return {

        "original_text": text,
        "textblob_output": corrected_text,
        "confidence_scores": confidence_scores,
        "bert_suggestions": bert_suggestions
    }