from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import pickle
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

app = FastAPI()

# Middleware for CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for simplicisty
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the trained model and vectorizer
model = pickle.load(open("fake_news_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

@app.get("/")
def read_root():
    return {"message": "Welcome to the Fake News Detection API"}

@app.post("/predict")
def predict(news: str = Form(...)):
    # Transform the input text
    input_features = vectorizer.transform([news])
    prediction = model.predict(input_features)
    result = "Fake" if prediction[0] == 0 else "True"
    return {"result": result}
