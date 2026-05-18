from textblob import TextBlob


def calculate_error_penalty(text):

    words = text.split()

    incorrect_count = 0

    for word in words:

        corrected = str(
            TextBlob(word).correct()
        )

        if corrected.lower() != word.lower():

            incorrect_count += 1

    penalty = incorrect_count * 0.15

    return round(penalty, 2)