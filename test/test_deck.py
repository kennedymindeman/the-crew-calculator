from src.card import Card, Suit
from src.deck import Deck


def test_blue_1_in_deck():
    assert Card(Suit.BLUE, 1) in Deck.ALL_CARDS
