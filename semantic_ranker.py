from sentence_transformers import (
    SentenceTransformer,
    util
)


# Load embedding model
embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def calculate_semantic_similarity(
    original,
    generated
):

    original_embedding = embedding_model.encode(
        original,
        convert_to_tensor=True
    )

    generated_embedding = embedding_model.encode(
        generated,
        convert_to_tensor=True
    )

    similarity = util.cos_sim(
        original_embedding,
        generated_embedding
    )

    return float(similarity[0][0])