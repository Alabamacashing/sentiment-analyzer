# 🎬 Movie Review Sentiment Analyzer

An AI-powered web app that analyzes movie reviews and predicts whether they are positive or negative.

## Built With
- Python
- Flask
- HuggingFace Transformers
- DistilBERT

## How It Works
1. User types a movie review
2. Flask server receives the text
3. DistilBERT transformer model analyzes the sentiment
4. Result returned instantly with confidence score

## Run Locally
```bash
pip install flask transformers tf-keras
python app.py
```
Then open http://127.0.0.1:5000

## Live Demo
[Try it here](https://sentiment-analyzer-4cpt.onrender.com)