class Card:

    def __init__(self, rank, suit, soft, hard):
        self.suit = suit
        self.rank = rank
        self.soft = soft
        self.hard = hard


class NumberCard(Card):

    def __init__(self, rank, suit):
        super().__init__(str(rank), suit, suit, rank)


class AceCard(Card):

    def __init__(self, rank, suit):
        super().__init__('A', suit, 1, 11)


class FaceCard(Card):

    def __init__(self, rank, suit):
        super().__init__({11: 'J', 12: 'Q', 13: 'K'}[rank], suit, 10, 10)


def alt_card_factory(rank, suit):
    if rank == 1:
        return AceCard(rank, suit)
    elif 2 <= rank < 11:
        return NumberCard(rank, suit)
    elif 11 <= rank < 14:
        return FaceCard(rank, suit)
    else:
        raise Exception("Rank is out of range")
