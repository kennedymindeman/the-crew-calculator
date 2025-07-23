from src.deck import Deck


class PlayerView:
    def __init__(self) -> None:
        self.possible_cards = set(Deck.ALL_CARDS)
