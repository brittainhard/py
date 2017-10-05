"""
A hash is an integer that reflects the complex value of an object. It is
distilled down to a hash which should usually contain all of the bits of the
source value.

The methods we are messing around with here are the __eq__ and __hash__ methods.
"""

import suits


class Potato:

    def __init__(self, apple):
        self.apple = apple

    def __eq__(self, other):
        return self.apple == other.apple

    def __hash__(self):
        return hash(self.apple)


a = Potato(1)
b = Potato(2)
