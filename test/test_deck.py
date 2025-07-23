from src.card import Card, Suit
from src.deck import Deck


def test_blue_1_in_deck():
    assert Card(Suit.BLUE, 1) in Deck.ALL_CARDS


def test_all_cards_in_deck_stack_after_constructor():
    deck = Deck()
    assert set(deck.draw_pile) == Deck.ALL_CARDS
