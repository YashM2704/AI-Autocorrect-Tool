# AI Autocorrect Tool
An AI-powered autocorrect system that combines classical NLP techniques with modern transformer models to deliver fast, context-aware text correction.
---
## Features
| Feature | Description |
|---|---|
| Spell Correction | Detects and fixes misspelled words using TextBlob |
| NLP Preprocessing | Tokenization, stopword removal, and text normalization via NLTK |
| Context-Aware Autocorrect | Understands surrounding words to suggest the most appropriate correction |
| BERT Integration | Leverages BERT's masked language modeling for intelligent word prediction |
| Streamlit UI | Clean, interactive web interface for real-time text correction |
---
## Tech Stack

- **Python** — Core language
- **TextBlob** — Spell checking and basic NLP
- **NLTK** — Natural language preprocessing
- **Transformers (HuggingFace)** — BERT model integration
- **BERT** — Context-aware word prediction via masked language modeling
- **Streamlit** — Interactive web UI
---
## Getting Started

### Prerequisites

Make sure you have Python 3.8+ installed.

### Installation

1. **Clone the repository**
   git clone https://github.com/your-username/ai-autocorrect.git
   cd ai-autocorrect
2. **Create a virtual environment** (recommended)
   python -m venv venv
   source venv/bin/activate        # On Windows: venv\Scripts\activate
3. **Install dependencies**
   pip install -r requirements.txt
4. **Download NLTK data**
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   nltk.download('wordnet')

### Running the App
streamlit run app.py

Then open your browser at `http://localhost:8501`.
---
## 📁 Project Structure

ai-autocorrect/
├── app.py                  # Streamlit UI entry point
├── autocorrect/
│   ├── spell_checker.py    # TextBlob-based spell correction
│   ├── preprocessor.py     # NLTK preprocessing pipeline
│   ├── bert_corrector.py   # BERT masked language model integration
│   └── utils.py            # Helper functions
├── requirements.txt        # Project dependencies
└── README.md

---
## 📦 Requirements
textblob
nltk
transformers
torch
streamlit
> Install all at once with `pip install -r requirements.txt`
---
## 🧠 How It Works

1. **Input text** is received through the Streamlit UI
2. **NLP Preprocessing** cleans and tokenizes the text using NLTK
3. **Spell Correction** runs a first pass with TextBlob to catch obvious typos
4. **BERT Context Analysis** uses masked language modeling to evaluate corrections in context — choosing the word that best fits the surrounding sentence
5. **Corrected text** is returned and displayed in the UI
---
## 📸 Demo
> _Add a screenshot or GIF of the Streamlit UI here_
---
## 🤝 Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.
1. Fork the repo
2. Create your feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add your feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a pull request

## 👤 Author
**YASH MAHAJAN**
- GitHub: [YashM2704](//github.com/YashM2704/AI-Autocorrect-Tool)
---

> Built with ❤️ using Python, TextBlob, NLTK, BERT, and Streamlit