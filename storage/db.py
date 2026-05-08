import sqlite3
from pathlib import Path

DB_PATH = Path("onchain.db")


def get_connection():
    return sqlite3.connect(DB_PATH)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    # wallet activity table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS wallet_activity (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        wallet TEXT,
        tx_hash TEXT,
        block_number INTEGER,
        value INTEGER,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # signals table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS signals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        wallet TEXT,
        signal_type TEXT,
        score REAL,
        block_number INTEGER,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()