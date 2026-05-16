import nltk
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
def ensure_nltk_resource(resource_path, download_name):
    try:
        nltk.data.find(resource_path)
    except LookupError:
        nltk.download(download_name, quiet=True)

ensure_nltk_resource('tokenizers/punkt_tab/english', 'punkt_tab')
ensure_nltk_resource('corpora/stopwords', 'stopwords')
ensure_nltk_resource('corpora/wordnet', 'wordnet')

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()
# Load stopwords
stop_words = set(stopwords.words('english'))

def preprocess_text(text):

    # Convert to lowercase
    text = text.lower()

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Tokenization
    tokens = word_tokenize(text)

    # Remove stopwords
    filtered_tokens = [
        word for word in tokens
        if word not in stop_words
    ]

    # Lemmatization
    lemmatized_tokens = [
        lemmatizer.lemmatize(word)
        for word in filtered_tokens
    ]

    return lemmatized_tokens