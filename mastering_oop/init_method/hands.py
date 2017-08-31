class BadHand:
    """This sucks because if you want to recreate it you have to add the items
    one by one back into the thing. The following one is better."""

    def __init__(self, dealer_card):
        self.dealer_card = dealer_card
        self.cards = []

    def hard_total(self):
        return sum(c.hard for c in self.cards)

    def soft_total(self):
        return sum(c.soft for c in self.cards)

    def __len__(self):
        return len(self.cards)


class GoodHand:
    """With this one we can load a sequence of cards at one time"""

    def __init__(self, dealer_card, *cards):
        self.dealer_card = dealer_card
        self.cards = list(cards)

    def hard_total(self):
        return sum(c.hard for c in self.cards)

    def soft_total(self):
        return sum(c.soft for c in self.cards)

    def __len__(self):
        return len(self.cards)


class CloneHand:
    """These last two are multi-strategy init methods, meaning that you can create a
    hand with two different methods. In CloneHand you can supply an existing hand
    object and grab the cards. It will copy the same card instances from the
    cloned hand, and you can test and make sure that the lists containing the
    items are thesame."""

    def __init__(self, *args, **kwargs):
        if len(args) == 1 and isinstance(args[0], CloneHand):
            # Clone the existing hand.
            other = args[0]
            self.dealer_card = other.dealer_card
            self.cards = other.cards
        else:
            # Build a new hand.
            dealer_card,*cards = args
            self.dealer_card = dealer_card
            self.cards = list(cards)


class StaticHand:

    def __init__(self, dealer_card, *cards):
        self.dealer_card = dealer_card
        self.cards = list(cards)

    @staticmethod
    def freeze(other):
        hand = StaticHand(other.dealer_card, *other.cards)
        return hand

    @staticmethod
    def split(other, card_0, card_1):
        hand_0 = StaticHand(other.dealer_card, other.cards[0], card_0)
        hand_1 = StaticHand(other.dealer_card, other.cards[1], card_1)
        return hand_0, hand_1

    def __str__(self):
        return ", ".join(map(str, self.cards))
