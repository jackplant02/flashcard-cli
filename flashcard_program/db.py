import sqlite3

DB_NAME = "flashcards.db"

def init_db():
    """Create the cards table it doesn't already exist."""
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute