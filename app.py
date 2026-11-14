from flask import Flask, request, render_template_string
import subprocess, re
from database import init_db, save_result
from datetime import datetime
init_db()
app = Flask(__name__)

HTML = """
<h2 style="text-align:center; font-family:arial;">AI Phishing & Fraud Detection</h2>
<div style="text-align:center;">
<form method="post">
<input name="text" style="width:300px; padding:10px;" placeholder="e.g. Your bank account blocked verify now"><br><br>
<input name="url" style="width:300px; padding:10px;" placeholder="e.g. http://fake-bank-verify.com"><br><br>
<button style="padding:10px 20px;">Check</button>
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
        save_result(text + " " + url, result, datetime.now().strftime("%Y-%m-%d %H:%M"))
    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(debug=True)
