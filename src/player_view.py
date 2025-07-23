from src.card import Card
from src.deck import Deck


class PlayerView:
    def __init__(self) -> None:
        self.possible_cards = set(Deck.ALL_CARDS)
        self.certain_cards = set()

    def mark_has_card(self, card: Card) -> None:
        self.possible_cards.discard(card)
        self.certain_cards.add(card)
