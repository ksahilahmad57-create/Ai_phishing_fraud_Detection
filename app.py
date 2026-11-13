from flask import Flask, request, render_template_string
import subprocess, re

app = Flask(__name__)

HTML = """
<h2 style="text-align:center; font-family:Arial">🛡️ AI Phishing & Fraud Detection</h2>
<div style="max-width:500px; margin:auto; font-family:Arial">
<form method="post">
<label>Message / SMS:</label><br>
<input name="text" style="width:100%; padding:10px" placeholder="e.g. Your bank account blocked verify now"><br><br>
<label>URL / Link:</label><br>
<input name="url" style="width:100%; padding:10px" placeholder="e.g. http://bank-verify-login123.com"><br><br>
<button style="width:100%; padding:12px; background:#007bff; color:white; border:none; font-size:16px">Check Now</button>
</form>
{% if result %}
<h3 style="text-align:center; background:#f0f0f0; padding:15px">{{ result }}</h3>
{% endif %}
</div>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        text = request.form.get("text", "")
        url = request.form.get("url", "")
        cmd = ["python", "predict.py", "--text", text, "--url", url]
        out = subprocess.run(cmd, capture_output=True, text=True).stdout
        result = out.replace("\n", " | ")
    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(debug=True)
