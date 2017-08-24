"""When creating factory functions, plain functions are good unless you need to
inherit from a higher level class. If you don't need to inherit, dont use a
class."""

from functools import partial

from suits import *
from cards import *


__all__ = ["card", "card_better_elif", "card_mapping", "factory_functions",
    "CardFactory"]


def card(rank, suit):
    if rank == 1:
        return AceCard('A', suit)
    elif 2 <= rank < 11:
        return NumberCard(str(rank), suit)
    elif 11 <= rank < 14:
        name = {11: "J", 12: "Q", 13: "K"}[rank]
        return FaceCard(name, suit)
    else:
        """The else clause is there to make explicit what inputs this function
        will handle"""
        raise Exception("Rank out of range.")


def card_better_elif(rank, suit):
    if rank == 1:
        return AceCard('A', suit)
    elif 2 <= rank < 11:
        return NumberCard(str(rank), suit)
    elif rank == 11:
        return FaceCard("J", suit)
    elif rank == 12:
        return FaceCard("Q", suit)
    elif rank == 13:
        return FaceCard("K", suit)
    else:
        """The else clause is there to make explicit what inputs this function
        will handle"""
        raise Exception("Rank out of range.")


def card_mapping(rank, suit):
    """Get the desired rank. If the rank isnt there by default, return a nubmer
    card"""
    class_ = {1: AceCard, 11: FaceCard, 12: FaceCard, 13: FaceCard}.get(rank, NumberCard)
    return class_(rank, suit)


def card_functools_mapping(rank, suit):
    part_class = {
        1: partial(AceCard, 'A'),
        11: partial(FaceCard, 'J'),
        12: partial(FaceCard, 'Q'),
        13: partial(FaceCard, 'K')
    }.get(rank, partial(NumberCard, str(rank)))
    return part_class(suit)


class CardFactory:
    """This class is designed to contain a 'fluent api'. That means that one
    function call happens after the next. In the example, its x.a().b(). This
    class is returning itself, which the next function uses to generate the
    card. We are containing this in one object for the sake of simplicity.
        It seems like the minute we decide to do a different API... I don't know
    how this woulf be useful exactly. A lot of these are just examples of stuff
    you can do with collections."""

    def rank(self, rank):
        self.class_, self.rank_str = {
            1: (AceCard, 'A'),
            11: (FaceCard, 'J'),
            12: (FaceCard, 'Q'),
            13: (FaceCard, 'K')
        }.get(rank, (NumberCard, str(rank)))
        return self
    
    def suit(self, suit):
        return self.class_(self.rank_str, suit)

    def get_deck(self):
        return [self.rank(r + 1).suit(s) for r in range(13) for s in (Club,
            Diamond, Heart, Spade)]


factory_functions = [card, card_better_elif, card_mapping,
    card_functools_mapping]
