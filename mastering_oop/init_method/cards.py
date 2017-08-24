"""Contains imformation on creating various kinds of superclasses based on the
Card class. We need to save this to be used later."""


__all__ = ["NumberCard", "AceCard", "FaceCard"]


class Card:

    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank
        self.soft, self.hard = self._points()


class NumberCard(Card):

    def _points(self):
        return int(self.rank), int(self.rank)


class AceCard(Card):

    def _points(self):
        return 1, 11


class FaceCard(Card):

    def _points(self):
        return 10, 10
