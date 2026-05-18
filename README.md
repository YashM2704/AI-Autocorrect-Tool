# AI Autocorrect Tool

**An intelligent, context-aware autocorrect system** that combines classical NLP techniques with modern transformer models to deliver fast, accurate, and explainable text corrections.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-FF4B4B?style=flat&logo=streamlit)
![Transformers](https://img.shields.io/badge/Hugging%20Face-Transformers-yellow?style=flat&logo=huggingface)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📋 Table of Contents

- [Features](#-features)
- [Tech Stack](#️-tech-stack)
- [Quick Start](#-quick-start)
- [Project Structure](#-project-structure)
- [System Architecture](#-system-architecture)
- [How It Works](#-how-it-works)
- [Requirements](#-requirements)
- [Contributing](#-contributing)
- [License](#-license)
- [Author](#-author)

---

## ✨ Features

- **Hybrid Spell Correction** — Rule-based + statistical correction using TextBlob
- **Advanced NLP Preprocessing** — Tokenization, normalization, stopword removal & lemmatization with NLTK
- **Context-Aware Intelligence** — BERT masked language modeling for semantically accurate suggestions
- **Real-time Interactive UI** — Modern, responsive Streamlit web interface
- **Confidence Scoring & Explainability** — Transparent feedback on every correction

---

## 🛠️ Tech Stack

| Component           | Technology                        |
|---------------------|-----------------------------------|
| **Core**            | Python 3.8+                       |
| **Spell Checking**  | TextBlob                          |
| **NLP Pipeline**    | NLTK                              |
| **AI Model**        | BERT (Hugging Face Transformers)  |
| **UI Framework**    | Streamlit                         |

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Git

### Installation

```bash
# Clone the repository
git clone https://github.com/YashM2704/AI-Autocorrect-Tool.git
cd AI-Autocorrect-Tool

# Create virtual environment
python -m venv venv
source venv/bin/activate          # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Download NLTK data
python -c "
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
"
```

### Run the Application

```bash
streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 📁 Project Structure

```
AI-Autocorrect-Tool/
├── app.py                    # Streamlit main application
├── autocorrect/
│   ├── spell_checker.py      # TextBlob spell correction
│   ├── preprocessor.py       # NLTK preprocessing
│   ├── bert_corrector.py     # BERT context-aware correction
│   └── utils.py              # Utility functions
├── requirements.txt
├── README.md
└── .streamlit/               # Optional Streamlit config
```

---

## � System Architecture

The system follows a layered pipeline architecture, processing input through multiple intelligent stages before returning a corrected result:

```
┌─────────────────────────────────────────┐
│           Client Applications           │
│   Web Client  │  Mobile App  │  API     │
└──────────────────┬──────────────────────┘
                   │
          ┌────────▼────────┐
          │ Input Validation │
          └────────┬────────┘
                   │
          ┌────────▼────────┐
          │ NLP Preprocessing│
          └────────┬────────┘
                   │
          ┌────────▼────────┐
          │  Error Detection │
          └────────┬────────┘
                   │
          ┌────────▼──────────────┐
          │ Candidate Generation  │
          └────────┬──────────────┘
                   │
          ┌────────▼──────────────┐
          │ Transformer Ranking   │
          │      Model (BERT)     │
          └────────┬──────────────┘
                   │
          ┌────────▼──────────────┐
          │  Grammar Correction   │
          └────────┬──────────────┘
                   │
          ┌────────▼────────┐
          │Confidence Scoring│
          └────────┬────────┘
                   │
          ┌────────▼──────────┐
          │ Explainability    │
          └────────┬──────────┘
                   │
          ┌────────▼────────┐
          │  REST API Layer  │
          └────────┬────────┘
                   │
          ┌────────▼──────────────┐
          │  Frontend / Web Client│
          └────────┬──────────────┘
                   │
          ┌────────▼──────────────┐
          │  Logging + Monitoring │
          └───────────────────────┘
```

---

## 🧠 How It Works

1. **Input** — Text received from the Streamlit UI
2. **Validation & Preprocessing** — Cleaned and tokenized using NLTK
3. **Initial Spell Check** — TextBlob detects obvious spelling mistakes
4. **Context Analysis** — BERT evaluates corrections within full sentence context
5. **Ranking & Scoring** — Best correction selected with confidence score
6. **Output** — Corrected text + explanation returned to user

---

## � Requirements

```txt
textblob
nltk
transformers
torch
streamlit
pandas
```

Install all at once:

```bash
pip install -r requirements.txt
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---
## 👤 Author

**YASH MAHAJAN**

- GitHub: [@YashM2704](https://github.com/YashM2704)

---

