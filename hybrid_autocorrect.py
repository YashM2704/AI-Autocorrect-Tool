from textblob_autocorrect import correct_spelling
from bert_autocorrect import bert_autocorrect
def hybrid_autocorrect(text):
    corrected_text = correct_spelling(text)
    print("\nTextBlob Correction:")
    print(corrected_text)
    original_words = text.split()
    corrected_words = corrected_text.split()
    suspicious_words = []

    for original, corrected in zip(original_words, corrected_words):
        if original != corrected:
            suspicious_words.append(corrected)
    bert_suggestions = []
    for word in suspicious_words:
        masked_sentence = corrected_text.replace(word, "[MASK]")
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