from dataclasses import dataclass
from enum import Enum, auto


class Suit(Enum):
    """Represents the five card suits.

    BLACK (Rockets): 4 cards (values 1-4)
    BLUE, GREEN, PINK, YELLOW: 9 cards each (values 1-9)
    """
    BLACK = auto()  # Rockets
    BLUE = auto()
    GREEN = auto()
    PINK = auto()
    YELLOW = auto()


@dataclass(frozen=True)
class Card:
    """An immutable playing card with a suit and value.

    Attributes:
        suit: The card's suit
        value: The card's numeric value (1-4 for BLACK, 1-9 for others)
    """
    suit: Suit
    value: int
