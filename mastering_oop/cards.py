from ..suits import *


__all__ = ["NumberCard", "AceCard", "FaceCard", "get_deck"]


class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.hard, self.soft = self._points()


class NumberCard(Card):

    def _points(self):
        return int(self.rank), int(self.rank)


class AceCard(Card):

    def _points(self):
        return 1, 11


class FaceCard(Card):

    def _points(self):
        return 10, 10


"""
Factory Pattern

The goal of a factory class is to wrap a complex class heirarchy and handle the complex
task of creating manufactured objects. We can also subclass factories in this way.

Right now using a function. A good idea is to start with functions, and then when you
need polymorphism, transfer everything to classes.

I've done these factory patterns a bunch before.
"""
def get_card(rank, suit):
    if rank == 1:
        return AceCard('A', suit)
    elif 2 <= rank <= 10:
        return NumberCard(str(rank), suit)
    elif 11 <= rank <= 13:
        name = {11: 'J', 12: 'Q', 13: 'K'}[rank]
        return FaceCard(name, suit)
    else:
        raise Exception("Rank out of range.")


def get_card_explicit(rank, suit):
    if rank == 1:
        return AceCard('A', suit)
    elif 2 <= rank <= 10:
        return NumberCard(str(rank), suit)
    elif rank == 11:
        return FaceCard('J', suit)
    elif rank == 12:
        return FaceCard('Q', suit)
    elif rank == 13:
        return FaceCard('K', suit)
    else:
        raise Exception("Rank out of range.")


"""
I did this to deal with the fact that the book was having me make a bunch of
different kinds of factories. I just passed the func.
"""
def get_deck(func):
    return [func(rank, suit) for rank in range(1, 14) for suit in (Club, Diamond, Heart, Spade)]


deck = get_deck(get_card_explicit)
