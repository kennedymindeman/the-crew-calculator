import random
from pytest import fixture
from src.deck import Deck
from src.player import Player


@fixture(name="deck")
def get_deck() -> Deck:
    random.seed(0)
    return Deck()


def test_player_has_player_view_equal_to_number_of_players():
    num_players = 4
    player = Player(player_id=0, num_players=num_players)
    assert len(player.player_views) == num_players


def test_cards_are_certain_after_draw(deck: Deck):
    num_players = 4
    player = Player(player_id=0, num_players=num_players)
    card = player.draw(deck)
    assert card in player.player_views[0].certain_cards


def test_cards_are_no_longer_possible_after_draw(deck: Deck):
    num_players = 4
    player = Player(player_id=0, num_players=num_players)
    card = player.draw(deck)
    assert card not in player.player_views[0].possible_cards


def test_cards_are_no_longer_possible_for_other_player_after_draw(deck: Deck):
    num_players = 4
    player_id = 0
    next_player_id = (player_id + 1) % num_players
    player = Player(player_id=player_id, num_players=num_players)
    card = player.draw(deck)
    assert card not in player.player_views[next_player_id].possible_cards


def test_hand_size_starts_at_0():
    player = Player(player_id=0, num_players=4)
    assert len(player.hand) == 0


def test_hand_size_goes_up_after_draw(deck: Deck):
    player = Player(player_id=0, num_players=4)
    player.draw(deck)
    assert len(player.hand) == 1


def test_playable_cards_in_empty_hand():
    player = Player(player_id = 0, num_players=4)
    assert player.get_playable_cards() == set()
