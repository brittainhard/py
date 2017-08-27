import random

from . import cards, card_factory
from .suits import Club, Diamond, Heart, Spade

class Deck:

    def __init__(self, factory_func):
        self.factory_func = factory_func
        self._cards = [factory_func(r + 1, s) for r in range(13) for s in (Club,
            Diamond, Heart, Spade)]
        random.shuffle(self._cards)

    def pop(self):
        return self._cards.pop()

    def __len__(self):
        """Although this is not a list at all, the central function is to act
        like a list, but with special methods attached to it, right?"""
        return len(self._cards)


deck_constructors = [Deck]
