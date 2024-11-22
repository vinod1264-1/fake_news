import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

# Load the datasets
true_data = pd.read_csv("True.csv")
fake_data = pd.read_csv("Fake.csv")

true_data["label"] = 1
fake_data["label"] = 0

# Combine and shuffle datasets
data = pd.concat([true_data, fake_data]).sample(frac=1).reset_index(drop=True)

# Split into features and labels
X = data["text"]
y = data["label"]

# Feature extraction
vectorizer = TfidfVectorizer(max_df=0.7, stop_words="english")
X_features = vectorizer.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_features, y, test_size=0.2, random_state=42)

# Train the model
model = LogisticRegression()
model.fit(X_train, y_train)

# Save the model and vectorizer
pickle.dump(model, open("fake_news_model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))
