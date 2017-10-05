HEART_SYMBOL = u'\u2661'
DIAMOND_SYMBOL = u'\u2662'
CLUB_SYMBOL = u'\u2663'
SPADE_SYMBOL = u'\u2664'


class Suit:

    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


Club = Suit("Club", CLUB_SYMBOL)
Diamond = Suit("Diamond", DIAMOND_SYMBOL)
Heart = Suit("Heart", HEART_SYMBOL)
Spade = Suit("Spade", SPADE_SYMBOL)
