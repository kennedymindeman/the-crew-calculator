from src.card import Card, Suit


def test_card_suit_matches_constructor():
    card = Card(Suit.BLUE, 9)
    assert card.suit == Suit.BLUE
