from dataclasses import dataclass
from enum import Enum, auto


class Suit(Enum):
    BLACK = auto()
    BLUE = auto()
    GREEN = auto()
    PINK = auto()
    YELLOW = auto()


@dataclass(frozen=True)
class Card:
    suit: Suit
    rank: int
