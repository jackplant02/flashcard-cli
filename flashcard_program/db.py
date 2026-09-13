import sqlite3

# this is the filename where SQLite stores the database
DB_NAME = "flashcards.db"

def init_db():
    """Create the cards table it doesn't already exist."""

    # opens a connection to 'flashcards.db' (creates the file if it doesn't exist)
    # and closes it automatically when done
    with sqlite3.connect(DB_NAME) as conn:
        # create a cursor object, which is used to send SQL commands to the database
        cursor = conn.cursor()
        # execute sql command (this one creates the 'cards' table, only if it doesn't exist)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cards (
                id INTEGER PRIMARY KEY,
                front TEXT NOT NULL,
                back TEXT NOT NULL
            )
        """)
        # Explicitly commit the changes 
        conn.commit()

        
def add_card(front, back):
    """Add a card to the database."""