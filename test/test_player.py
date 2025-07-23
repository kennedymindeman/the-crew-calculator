from src.player import Player


def test_player_has_player_view_equal_to_number_of_players():
    num_players = 4
    player = Player(player_id=0, num_players=num_players)
    assert len(player.player_views) == num_players
