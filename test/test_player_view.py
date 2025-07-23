from src.deck import Deck
from src.player_view import PlayerView


def test_everything_unknown_before_draw():
    player_view = PlayerView()
    assert player_view.possible_cards == Deck.ALL_CARDS
