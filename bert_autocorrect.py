from transformers import pipeline


fill_mask = pipeline(
    "fill-mask",
    model="bert-base-uncased"
)


def bert_autocorrect(text):

    results = fill_mask(text, top_k=5)

    predictions = []

    for result in results:

        predictions.append(result["sequence"])

    return predictions