from src.card import Card, Suit
from src.deck import Deck
from src.player_view import PlayerView


def test_everything_unknown_before_draw():
    player_view = PlayerView()
    assert player_view.possible_cards == Deck.ALL_CARDS


def test_no_cards_known_before_draw():
    player_view = PlayerView()
    assert player_view.certain_cards == set()


def test_mark_has_card_removes_card_from_possible_cards():
    card = Card(Suit.BLACK, 3)
    player_view = PlayerView()
    player_view.mark_has_card(card)
    assert card not in player_view.possible_cards


def test_mark_has_card_adds_it_to_certain_cars():
    card = Card(Suit.BLACK, 3)
    player_view = PlayerView()
    player_view.mark_has_card(card)
    assert card in player_view.certain_cards


def test_eliminate_card_removes_it_from_possible_cards():
    card = Card(Suit.BLACK, 3)
    player_view = PlayerView()
    player_view.eliminate_card(card)
    assert card not in player_view.possible_cards


def test_eliminate_card_removes_it_from_certain_cards():
    card = Card(Suit.BLACK, 3)
    player_view = PlayerView()
    player_view.mark_has_card(card)
    player_view.eliminate_card(card)
    assert card not in player_view.certain_cards
