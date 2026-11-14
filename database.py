import sqlite3

def init_db():
    conn = sqlite3.connect("phishing.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS results
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  message TEXT,
                  result TEXT,
                  date TEXT)''')
    conn.commit()
    conn.close()

def save_result(message, result, date):
    conn = sqlite3.connect("phishing.db")
    c = conn.cursor()
    c.execute("INSERT INTO results (message, result, date) VALUES (?, ?, ?)",
              (message, result, date))
    conn.commit()
    conn.close()

def get_all_results():
    conn = sqlite3.connect("phishing.db")
    c = conn.cursor()
    c.execute("SELECT * FROM results ORDER BY id DESC")
    rows = c.fetchall()
    conn.close()
    return rows

if __name__ == "__main__":
    init_db()
    print("Database created!")
