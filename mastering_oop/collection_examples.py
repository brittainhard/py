"""
Going to contain a lot of examples of collection classes. No need to worry about
testing out the code. Only make sure that there are no syntactical errors? Nah,
add some tests for the hell of it.

There are three general strategies for designing collection objects.

1) Wrap:
    An existing kind of collection. Just providing methods on top of it.
2) Extend:
    Normal subclass definition. 
3) Invent:
   Making a collection from scratch.
"""
import random

from suits import *
from subclass_init import *


# Wrapper example
class DeckWrapper:
    """
    The deck class now has its own implementation  of pop.

    Wrappers contain elements that are delegated to the base class. These can
    become wordy.
    """

    def __init__(self):
        self._cards = [get_card(r + 1, s) for r in range(13) for s in (Club,
            Diamond, Heart, Spade)]

    def pop(self):
        return self._cards.pop()


def test_wrapper():
    d = DeckWrapper()
    hand = [d.pop(), d.pop()]


class DeckExtension(list):
    """
    This is an extension of list.

    This has literally never occurred to me before. Wow.
    """

    def __init__(self):
        super().__init__(get_card(r + 1, s) for r in range(13) for s in (Club,
            Heart, Diamond, Spade))
        random.shuffle(self)


def test_extension():
    deck = DeckExtension()

deck1 = DeckExtension()

class DeckExtension2(list):

    def __init__(self, decks=1):
        self.extend(get_card(r + 1, s) for r in range(13) for s in (Club,
            Heart, Diamond, Spade) for d in range(decks))
        random.shuffle(self)
        burn = random.randint(1, 52)
        for i in range(burn):
            self.pop()


def test_extension2():
    deck = DeckExtension2(2)

deck2 = DeckExtension2(2)

Deck = DeckExtension
