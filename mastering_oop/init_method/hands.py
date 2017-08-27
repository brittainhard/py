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
