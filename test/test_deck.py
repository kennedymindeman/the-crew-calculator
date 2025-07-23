import random
from src.card import Card, Suit
from src.deck import Deck


def test_blue_1_in_deck():
    assert Card(Suit.BLUE, 1) in Deck.ALL_CARDS


def test_all_cards_in_deck_stack_after_constructor():
    deck = Deck()
    assert set(deck.draw_pile) == Deck.ALL_CARDS


def test_deck_shuffle_results_in_unique_deck():
    random.seed(0)
    decks = (Deck(), Deck())
    for deck in decks:
        deck.shuffle()
    assert decks[0].draw_pile != decks[1].draw_pile
