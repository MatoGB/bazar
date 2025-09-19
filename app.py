# app.py
from __future__ import annotations
import os
import sqlite3
from pathlib import Path
from flask import Flask, g, render_template, request, redirect, url_for, abort, jsonify

# --- Config básica ---
BASE_DIR = Path(__file__).resolve().parent
INSTANCE_DIR = BASE_DIR / "instance"
DB_PATH = INSTANCE_DIR / "app.db"

def create_app():
    app = Flask(__name__, instance_path=str(INSTANCE_DIR), instance_relative_config=True)
    app.config.update(
        SECRET_KEY=os.environ.get("SECRET_KEY", "dev"),
        DATABASE=str(DB_PATH),
    )

    # Asegurar que la carpeta instance exista
    INSTANCE_DIR.mkdir(parents=True, exist_ok=True)

    # Asegurar que el archivo de DB exista (vacío, sin tablas)
    if not DB_PATH.exists():
        # Crea un archivo SQLite vacío
        conn = sqlite3.connect(DB_PATH)
        conn.close()

    # --- Conexión a DB por request (sin ORM, simple y claro) ---
    def get_db():
        if "db" not in g:
            g.db = sqlite3.connect(app.config["DATABASE"])
            g.db.row_factory = sqlite3.Row
        return g.db

    @app.teardown_appcontext
    def close_db(exc):
        db = g.pop("db", None)
        if db is not None:
            db.close()

    # --- Rutas mínimas ---
    @app.route("/")
    def home():
        return render_template("index.html")

    return app

app = create_app()

if __name__ == "__main__":
    # Solo para desarrollo (no usar en prod)
    app.run(debug=True)
