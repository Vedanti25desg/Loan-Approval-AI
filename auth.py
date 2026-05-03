import sqlite3
import hashlib
import os

DB_PATH = "loansense_users.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Create users table if it doesn't exist."""
    conn = get_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id       INTEGER PRIMARY KEY AUTOINCREMENT,
            name     TEXT    NOT NULL,
            email    TEXT    NOT NULL UNIQUE,
            password TEXT    NOT NULL,
            created  DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def hash_password(password: str) -> str:
    return hashlib.sha256(password.strip().encode()).hexdigest()

def register_user(name: str, email: str, password: str) -> dict:
    """
    Returns {"success": True} or {"success": False, "error": "..."}
    """
    init_db()
    try:
        conn = get_connection()
        conn.execute(
            "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
            (name.strip(), email.strip().lower(), hash_password(password))
        )
        conn.commit()
        conn.close()
        return {"success": True}
    except sqlite3.IntegrityError:
        return {"success": False, "error": "Email already registered. Please sign in."}
    except Exception as e:
        return {"success": False, "error": str(e)}

def login_user(email: str, password: str) -> dict:
    """
    Returns {"success": True, "name": "..."} or {"success": False, "error": "..."}
    """
    init_db()
    conn = get_connection()
    row = conn.execute(
        "SELECT name FROM users WHERE email = ? AND password = ?",
        (email.strip().lower(), hash_password(password))
    ).fetchone()
    conn.close()
    if row:
        return {"success": True, "name": row["name"]}
    return {"success": False, "error": "Invalid email or password."}