import sqlite3
from pathlib import Path

# Database file in same folder
DB_PATH = Path(__file__).with_name("finance.db")

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_conn() as conn:
        conn.execute("PRAGMA foreign_keys = ON;")

        conn.execute("""
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL
        );
        """)

        conn.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            amount_cents INTEGER NOT NULL,
            category_id INTEGER NOT NULL,
            merchant TEXT,
            note TEXT,
            FOREIGN KEY (category_id) REFERENCES categories(id)
        );
        """)

        conn.execute("CREATE INDEX IF NOT EXISTS idx_date ON transactions(date);")

def ensure_category(name: str) -> int:
    with get_conn() as conn:
        conn.execute("INSERT OR IGNORE INTO categories(name) VALUES (?);", (name,))
        row = conn.execute("SELECT id FROM categories WHERE name = ?;", (name,)).fetchone()
        return row["id"]

def add_transaction(date: str, amount_cents: int, category: str, merchant: str = "", note: str = ""):
    cat_id = ensure_category(category)

    with get_conn() as conn:
        conn.execute(
            """
            INSERT INTO transactions(date, amount_cents, category_id, merchant, note)
            VALUES (?, ?, ?, ?, ?);
            """,
            (date, amount_cents, cat_id, merchant, note)
        )

def get_all_transactions():
    with get_conn() as conn:
        rows = conn.execute("""
            SELECT t.id, t.date, t.amount_cents, c.name AS category
            FROM transactions t
            JOIN categories c ON t.category_id = c.id
            ORDER BY t.date DESC;
        """).fetchall()
        return rows
