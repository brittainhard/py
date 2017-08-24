"""When creating factory functions, plain functions are good unless you need to
inherit from a higher level class. If you don't need to inherit, dont use a
class."""

from suits import *
from cards import *


def card(rank, suit):
    if rank == 1:
        return AceCard('A', suit)
    elif 2 <= rank < 11:
        return NumberCard(str(rank), suit)
    elif 11 <= rank < 14:
        name = {11: "J", 12: "Q", 13: "K"}[rank]
        return FaceCard(name, suit)
    else:
        raise Exception("Rank out of range.")


deck = [card(rank, suit) for rank in range(1, 11) for suit in (Club, Diamond,
    Heart, Spade)]
print(deck)


def test_card_factory():
    number_card = card(3, Spade)
    ace_card = card(1, Heart)
    face_card = card(11, Club)
    assert type(number_card) == NumberCard
    assert type(ace_card) == AceCard
    assert type(face_card) == FaceCard
