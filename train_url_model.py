"""Train a phishing URL classifier (handcrafted features + Random Forest).

Expects data/urls.csv with columns: url,label   (1 = phishing, 0 = legitimate)
"""
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

from url_features import features_dataframe

DATA_PATH = "data/urls.csv"
MODEL_PATH = "models/url_model.joblib"


def main():
    df = pd.read_csv(DATA_PATH).dropna()
    X = features_dataframe(df["url"])
    y = df["label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )

    model = RandomForestClassifier(n_estimators=200, random_state=42, class_weight="balanced")
    model.fit(X_train, y_train)

    print(classification_report(y_test, model.predict(X_test), zero_division=0))
    joblib.dump({"model": model, "columns": list(X.columns)}, MODEL_PATH)
    print(f"Saved model to {MODEL_PATH}")


if __name__ == "__main__":
    main()
