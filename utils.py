import Levenshtein
def calculate_similarity(word1, word2):
    distance = Levenshtein.distance(word1, word2)
    max_length = max(len(word1), len(word2))
    similarity_score = (
        1 - (distance / max_length)
    )
    return round(similarity_score, 2)