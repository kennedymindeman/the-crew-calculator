from src.card import Card, Suit
from src.deck import Deck
from src.player_view import PlayerView


class Player:
    def __init__(self, *, player_id: int, num_players: int) -> None:
        self.hand = set()
        self.player_id = player_id
        self.player_views = [PlayerView() for _ in range(num_players)]

    def draw(self, deck: Deck) -> Card:
        card = deck.deal()
        for player_view in self.player_views:
            player_view.eliminate_card(card)
        self.player_views[self.player_id].mark_has_card(card)
        self.hand.add(card)
        return card

    def get_playable_cards(self, suit : Suit | None = None) -> set[Card]:
        cards_in_suit = {card for card in self.hand if card.suit == suit}
        if cards_in_suit:
            return cards_in_suit
        return self.hand
