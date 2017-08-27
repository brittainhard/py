class GameStrategy:

    def insurance(self, hand):
        return False

    def split(self, hand):
        return False

    def double(self, hand):
        return False

    def hit(self, hand):
        return sum(card.hard for card in hand.cards) <= 17
