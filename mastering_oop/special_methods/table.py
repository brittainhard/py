from .hands import GoodHand as Hand


class Table:

    def __init__(self):
        self.deck = deck

    def place_bet(self, amount):
        print("Bet ", amount)

    def get_hand(self):
        try:
            self.hand = Hand(deck.pop(), deck.pop(), deck.pop())
            self.hole_card = d.pop()
        except IndexError:
            # Out of cards, needs reshuffle.
            self.deck = deck
            return self.get_hand()
        print("Deal ", self.hand)
        return self.hand

    def card_insure(self, hand):
        return hand.dealer_card.insure
