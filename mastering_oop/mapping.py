from functools import partial
from cards import *


def mapping_get_card(rank, suit):
    # From this dictionary get the value associated with the number. Default is
    # number card if it aint in the dict. In this case I think that the mapping
    # is the object that the arguments are applied to.
    #
    # This is broken because it does not give the letter associated with that
    # card.
    class_ = {
        1: AceCard,
        11: FaceCard,
        12: FaceCard,
        13: FaceCard
    }.get(rank, NumberCard)
    return class_(rank, suit)


def two_parallell_mappings(rank, suit):
    """
    Add another mapping that solves the above problem. Pretty ugly but it works.
    Next one is mapping with tuple, which looks better.
    """
    class_ = {
        1: AceCard,
        11: FaceCard,
        12: FaceCard,
        13: FaceCard
    }.get(rank, NumberCard)
    rank_str = {
        11: 'J',
        12: 'Q',
        13: 'K'
    }.get(rank, str(rank))
    return class_(rank_str, suit)


def tuple_mapping(rank, suit):
    """
    Ugly, but better.
    """
    class_, rank_str = {
        1: (AceCard, 'A'),
        11: (FaceCard, 'J'),
        12: (FaceCard, 'Q'),
        13: (FaceCard, 'K')
    }.get(rank, (NumberCard, str(rank)))
    return class_(rank_str, suit)


def partial_mapping(rank, suit):
    """
    No friggin idea of how this is working, confusing as hell.

    So basically, what we have here is that its return a partial function.
    To make a partial function, you have to supply the arguments to call. In
    this case, when you create the partial, you will supply it with the
    arguments as soon as you call the partial function.
    """
    partial_class = {
        1: partial(AceCard, 'A'),
        11: partial(FaceCard, 'J'),
        12: partial(FaceCard, 'Q'),
        13: partial(FaceCard, 'K')
    }.get(rank, partial(NumberCard, str(rank)))
    return partial_class(suit)


deck = get_deck(partial_mapping)[0]
print(dir(deck))
