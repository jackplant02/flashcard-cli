import pytest
from flashcard_program.db import add_card, get_all_cards, init_db

@pytest.fixture
def test_db(tmp_path):
    """Creates a temporary SQLite database path and initializes table."""

    db_path = str(tmp_path / "test_flashcards.db")

    init_db(db_path)

    return db_path

def test_init_db_creates_empty_table(test_db):
    """Verify that a freshly initialized database contains zero cards."""
    cards = get_all_cards(test_db)
    assert cards == []