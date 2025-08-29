import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "bazar.db"

schema = """
CREATE TABLE IF NOT EXISTS products (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  description TEXT NOT NULL,
  price REAL NOT NULL
);
"""

seed = [
    ("Mate Imperial", "Mate de calabaza con virola de acero.", 1499.0),
    ("Termo 1L", "Termo de acero inoxidable con pico cebador.", 3299.0),
]

def main():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.executescript(schema)
    cur.execute("DELETE FROM products")
    cur.executemany(
        "INSERT INTO products (name, description, price) VALUES (?, ?, ?)", seed
    )
    conn.commit()
    conn.close()
    print("Base creada y productos cargados en", DB_PATH)

if __name__ == "__main__":
    main()
