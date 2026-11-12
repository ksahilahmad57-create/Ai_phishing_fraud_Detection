"""Train an email/SMS phishing classifier (TF-IDF + Logistic Regression).

Expects data/messages.csv with columns: text,label   (1 = phishing/fraud, 0 = safe)
"""
import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

DATA_PATH = "data/messages.csv"
MODEL_PATH = "models/text_model.joblib"


def main():
    df = pd.read_csv(DATA_PATH).dropna()
    X_train, X_test, y_train, y_test = train_test_split(
        df["text"], df["label"], test_size=0.25, random_state=42, stratify=df["label"]
    )

    model = Pipeline([
        ("tfidf", TfidfVectorizer(lowercase=True, stop_words="english", ngram_range=(1, 2))),
        ("clf", LogisticRegression(max_iter=1000, class_weight="balanced")),
    ])
    model.fit(X_train, y_train)

    print(classification_report(y_test, model.predict(X_test), zero_division=0))
    joblib.dump(model, MODEL_PATH)
    print(f"Saved model to {MODEL_PATH}")


if __name__ == "__main__":
    main()
