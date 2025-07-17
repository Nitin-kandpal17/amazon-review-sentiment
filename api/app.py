# api/app.py

from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer

# Load model and vectorizer
model = joblib.load("models/naive_bayes.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

app = FastAPI()

class Review(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"msg": "Amazon Sentiment API is running!"}

@app.post("/predict")
def predict_sentiment(review: Review):
    text = review.text
    vector = vectorizer.transform([text])
    pred = model.predict(vector)[0]

    sentiment = {0: "Negative", 1: "Neutral", 2: "Positive"}
    return {
        "text": text,
        "predicted_class": int(pred),
        "sentiment": sentiment.get(pred, "Unknown")
    }
