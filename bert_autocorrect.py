from transformers import pipeline


# Load BERT fill-mask pipeline
fill_mask = pipeline(
    "fill-mask",
    model="bert-base-uncased"
)


def bert_autocorrect(text):

    results = fill_mask(text, top_k=5)

    predictions = []

    for result in results:

        predicted_sentence = result['sequence']

        predictions.append(predicted_sentence)

    return predictions