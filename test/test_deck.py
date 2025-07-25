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


def test_dealt_card_not_in_draw_pile():
    random.seed(0)
    deck = Deck()
    card = deck.deal()
    assert card not in deck.draw_pile


def test_deck_is_empty_after_all_cards_are_dealt():
    deck = Deck()
    while deck.draw_pile:
        deck.deal()
    assert deck.is_empty()
