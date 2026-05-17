from hybrid_autocorrect import hybrid_autocorrect
text = input("Enter sentence: ")
result = hybrid_autocorrect(text)
print("\nFinal Results\n")
print("Original Text:")
print(result["original_text"])
print("\nTextBlob Corrected:")
print(result["textblob_output"])
print("\nBERT Suggestions:")
for suggestion in result["bert_suggestions"]:
    print("\nMasked Sentence:")
    print(suggestion["masked_sentence"])
    print("\nPredictions:")
    for prediction in suggestion["predictions"]:
        print(prediction)