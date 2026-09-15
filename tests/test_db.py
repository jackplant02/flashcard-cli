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


def test_add_single_card(test_db):
    """Verify adding a card stores the row and assigns ID 1."""
    add_card("Hello", "Bonjour", db_name=test_db)

    cards = get_all_cards(test_db)
    assert len(cards) == 1

    card_id, front, back = cards[0]
    assert card_id == 1
    assert front == "Hello"
    assert back == "Bonjour"


def test_add_multiple_cards(test_db):
    """Verify multiple inserts auto-increment IDs and preserve entries."""
    add_card("Q1", "A1", db_name=test_db)
    add_card("Q2", "A2", db_name=test_db)

    cards = get_all_cards(test_db)
    assert len(cards) == 2
    assert cards[0] == (1, "Q1", "A1")
    assert cards[1] == (2, "Q2", "A2")


def test_init_db_does_not_wipe_data(test_db):
    """Verify calling init_db again doesn't destroy existing rows."""
    add_card("Keep", "Me", db_name=test_db)

    # Run init_db a second time
    init_db(test_db)

    cards = get_all_cards(test_db)
    assert len(cards) == 1
    assert cards[0][1] == "Keep"