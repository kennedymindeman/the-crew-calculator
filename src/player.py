from src.card import Card
from src.deck import Deck
from src.player_view import PlayerView


class Player:
    def __init__(self, *, player_id: int, num_players: int) -> None:
        self.player_id = player_id
        self.player_views = [PlayerView() for _ in range(num_players)]

    def draw(self, deck: Deck) -> Card:
        card = deck.deal()
        for player_view in self.player_views:
            player_view.eliminate_card(card)
        self.player_views[self.player_id].mark_has_card(card)
        return card
