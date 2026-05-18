# AI Autocorrect Tool

**An intelligent, context-aware text correction system** that seamlessly blends classical NLP with state-of-the-art transformer models for fast, accurate, and explainable autocorrection.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-FF4B4B?style=flat&logo=streamlit)
![HuggingFace](https://img.shields.io/badge/Hugging%20Face-Transformers-yellow?style=flat&logo=huggingface)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## ✨ Features

- **Hybrid Spell Correction** — Combines rule-based and statistical methods (TextBlob) with deep learning
- **Advanced NLP Preprocessing** — Tokenization, normalization, stopword removal, and lemmatization using NLTK
- **Context-Aware Suggestions** — BERT masked language modeling understands sentence context for intelligent corrections
- **Real-time Interactive UI** — Clean, responsive Streamlit interface with instant feedback
- **High Accuracy & Transparency** — Confidence scoring and clear explanations for every suggestion

---

## 🛠️ Tech Stack

| Layer              | Technology                          |
|--------------------|-------------------------------------|
| **Core Language**  | Python 3.8+                        |
| **Spell Checking** | TextBlob                           |
| **NLP Pipeline**   | NLTK                               |
| **AI Model**       | BERT (Hugging Face Transformers)   |
| **Framework**      | Streamlit                          |
| **Visualization**  | Streamlit + Custom CSS             |

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Git

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/YashM2704/AI-Autocorrect-Tool.git
cd AI-Autocorrect-Tool

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Download NLTK data
python -c "
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
"