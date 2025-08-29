from flask import Flask, render_template
import sqlite3
from pathlib import Path

app = Flask(__name__)

DB_PATH = Path(__file__).parent / "bazar.db"

def get_products():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    rows = conn.execute("SELECT id, name, description, price FROM products ORDER BY id").fetchall()
    conn.close()
    return rows

@app.route("/")
def index():
    products = get_products()
    return render_template("index.html", products=products)

@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
