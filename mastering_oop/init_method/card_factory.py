"""When creating factory functions, plain functions are good unless you need to
inherit from a higher level class. If you don't need to inherit, dont use a
class."""

from functools import partial

from suits import *
from cards import *


__all__ = ["card", "card_better_elif", "card_mapping", "factory_functions"]


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


factory_functions = [card, card_better_elif, card_mapping, card_functools_mapping]
