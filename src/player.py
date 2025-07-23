from src.player_view import PlayerView


class Player:
    def __init__(self, *, player_id: int, num_players: int) -> None:
        self.player_views = [PlayerView() for _ in range(num_players)]
