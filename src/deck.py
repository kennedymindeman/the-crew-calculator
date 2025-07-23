from random import shuffle
from src.card import Card, Suit


class Deck:
    BLACK_CARDS = frozenset(Card(Suit.BLACK, rank) for rank in range(1, 5))
    BLUE_CARDS = frozenset(Card(Suit.BLUE, rank) for rank in range(1, 10))
    GREEN_CARDS = frozenset(Card(Suit.GREEN, rank) for rank in range(1, 10))
    PINK_CARDS = frozenset(Card(Suit.PINK, rank) for rank in range(1, 10))
    YELLOW_CARDS = frozenset(Card(Suit.YELLOW, rank) for rank in range(1, 10))
    ALL_CARDS = BLACK_CARDS | BLUE_CARDS | GREEN_CARDS | PINK_CARDS | YELLOW_CARDS

    def __init__(self) -> None:
        self.draw_pile = list(Deck.ALL_CARDS)

    def shuffle(self) -> None:
        shuffle(self.draw_pile)

    def deal(self) -> Card:
        return self.draw_pile.pop()

    def is_empty(self) -> bool:
        return len(self.draw_pile) == 0
