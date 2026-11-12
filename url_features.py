"""Extract numeric features from a URL for phishing detection."""
import re
from urllib.parse import urlparse

import pandas as pd

SUSPICIOUS_WORDS = [
    "login", "verify", "update", "secure", "account", "bank", "confirm",
    "password", "signin", "paypal", "free", "bonus", "wallet", "suspend",
]
SHORTENERS = ("bit.ly", "tinyurl.com", "goo.gl", "t.co", "ow.ly", "is.gd")
IP_PATTERN = re.compile(r"^\d{1,3}(\.\d{1,3}){3}$")


def extract_features(url: str) -> dict:
    url = str(url).strip()
    parsed = urlparse(url if "://" in url else "http://" + url)
    host = parsed.netloc.lower().split("@")[-1].split(":")[0]
    path = parsed.path
    lower = url.lower()

    return {
        "url_length": len(url),
        "host_length": len(host),
        "path_length": len(path),
        "num_dots": url.count("."),
        "num_hyphens": url.count("-"),
        "num_digits": sum(c.isdigit() for c in url),
        "num_special": sum(url.count(c) for c in "@?&=_%"),
        "has_at": int("@" in url),
        "has_ip": int(bool(IP_PATTERN.match(host))),
        "is_https": int(parsed.scheme == "https"),
        "num_subdomains": max(host.count(".") - 1, 0),
        "suspicious_words": sum(w in lower for w in SUSPICIOUS_WORDS),
        "is_shortener": int(host in SHORTENERS),
        "double_slash_in_path": int("//" in path),
    }


def features_dataframe(urls) -> pd.DataFrame:
    return pd.DataFrame([extract_features(u) for u in urls])
