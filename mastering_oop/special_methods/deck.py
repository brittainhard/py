import random
from . import cards
from .card_factory import card_better_elif
from .suits import Club, Diamond, Heart, Spade

class Deck:

    def __init__(self):
        self._cards = [card_better_elif(r + 1, s) for r in range(13) for s in (Club,
            Diamond, Heart, Spade)]
        random.shuffle(self._cards)

    def pop(self):
        return self._cards.pop()

    def __len__(self):
        """Although this is not a list at all, the central function is to act
        like a list, but with special methods attached to it, right?"""
        return len(self._cards)


class ListDeck(list):
    """Actually inhereting from a list here, but from above we can also make
    that object act like a list. In this way you can modify the underlying
    things if you wanted to."""

    def __init__(self):
        super().__init__(card_better_elif(r + 1, s) for r in range(13) for s in (Club,
            Diamond, Heart, Spade))
        random.shuffle(self)


class DealerDeck(list):
    """This is for dealing blackjack from a shoe."""

    def __init__(self, decks=1):
        super().__init__()
        for i in range(decks):
            self.extend(card_better_elif(r + 1, s) for r in range(13) for s in (Club,
                Diamond, Heart, Spade))
        random.shuffle(self)
        burn = random.randint(1, 52)
        for i in range(burn):
            self.pop()


deck_constructors = [Deck, ListDeck, DealerDeck]
