# 🛡️ Ai_phishing_fraud_Detection

An AI-based system that detects **phishing emails**, **suspicious URLs**, and **fraudulent messages** using machine learning.

## ✨ Features

- **Message/Email classifier**: TF-IDF + Logistic Regression flags phishing and scam text.
- **URL classifier**: extracts 14 URL features (length, IP address, `@` symbol, suspicious keywords, subdomains, HTTPS, shorteners, etc.) and uses a Random Forest.
- **Risk score**: every prediction returns a probability (0 to 1) with a verdict: *Looks safe*, *Suspicious*, or *Phishing/Fraud*.
- **Simple command-line tool** for quick checks.

## 📁 Project Structure

```
Ai_phishing_fraud_Detection/
├── data/
│   ├── messages.csv        # text,label
│   └── urls.csv            # url,label
├── models/                 # trained models are saved here
├── src/
│   ├── url_features.py     # URL feature extraction
│   ├── train_text_model.py # train message/email model
│   ├── train_url_model.py  # train URL model
│   └── predict.py          # CLI to check text or URLs
├── requirements.txt
└── README.md
```

## ⚙️ Installation

```bash
git clone https://github.com/ksahilahmad57-create/Ai_phishing_fraud_Detection.git
cd Ai_phishing_fraud_Detection
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## 🚀 Usage

**1. Train the models**

```bash
python src/train_text_model.py
python src/train_url_model.py
```

**2. Check a message or URL**

```bash
python src/predict.py --text "Your account is suspended. Verify your password now."
python src/predict.py --url "http://secure-login.bank-verify.xyz/signin"
python src/predict.py --text "Meeting at 3 PM" --url "https://github.com"
```

**Example output**

```
Message risk score: 0.91 -> PHISHING / FRAUD (high risk)
URL risk score: 0.80 -> PHISHING / FRAUD (high risk)
```

## 📊 Datasets

The included CSV files are **tiny samples** so the project runs out of the box. For real accuracy, replace them with larger datasets (keep the same column names, `1` = phishing, `0` = safe):

- [PhishTank](https://phishtank.org/) – verified phishing URLs
- [Kaggle: Phishing Site URLs / Phishing Email Dataset](https://www.kaggle.com/datasets)
- [SMS Spam Collection (UCI)](https://archive.ics.uci.edu/dataset/228/sms+spam+collection)

## 🧠 How It Works

| Input | Method | Model |
|-------|--------|-------|
| Email / SMS text | TF-IDF (1–2 word n-grams) | Logistic Regression |
| URL | Handcrafted lexical features | Random Forest |

## 🗺️ Roadmap

- [ ] Train on large real-world datasets
- [ ] Add BERT-based text model
- [ ] Domain age / WHOIS and SSL checks
- [ ] Web app (Streamlit or Flask)
- [ ] Browser extension

## ⚠️ Disclaimer

This is an educational project. Predictions are probabilistic and can be wrong, so don't rely on it as your only protection.

## 📜 License

MIT License. Free to use and modify.
