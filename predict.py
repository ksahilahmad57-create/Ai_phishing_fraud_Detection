"""Check a message or URL for phishing.

Usage:
    python src/predict.py --text "Your account is suspended, verify now"
    python src/predict.py --url "http://secure-login.example-bank.xyz/verify"
"""
import argparse
import os

import joblib

from url_features import features_dataframe

TEXT_MODEL = "models/text_model.joblib"
URL_MODEL = "models/url_model.joblib"


def verdict(prob: float) -> str:
    if prob >= 0.7:
        return "PHISHING / FRAUD (high risk)"
    if prob >= 0.4:
        return "SUSPICIOUS (be careful)"
    return "LOOKS SAFE"


def check_text(text: str):
    model = joblib.load(TEXT_MODEL)
    prob = model.predict_proba([text])[0][1]
    print(f"Message risk score: {prob:.2f} -> {verdict(prob)}")


def check_url(url: str):
    bundle = joblib.load(URL_MODEL)
    X = features_dataframe([url])[bundle["columns"]]
    prob = bundle["model"].predict_proba(X)[0][1]
    print(f"URL risk score: {prob:.2f} -> {verdict(prob)}")


def main():
    parser = argparse.ArgumentParser(description="AI phishing & fraud detector")
    parser.add_argument("--text", help="Email or message text to check")
    parser.add_argument("--url", help="URL to check")
    args = parser.parse_args()

    if not (args.text or args.url):
        parser.error("Provide --text and/or --url")
    if args.text:
        if not os.path.exists(TEXT_MODEL):
            parser.error("Text model not found. Run: python src/train_text_model.py")
        check_text(args.text)
    if args.url:
        if not os.path.exists(URL_MODEL):
            parser.error("URL model not found. Run: python src/train_url_model.py")
        check_url(args.url)


if __name__ == "__main__":
    main()
