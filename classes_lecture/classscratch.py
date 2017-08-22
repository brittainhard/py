import sys
from example import Circle


class Potato:

    __slots__ = ["apple"]

    def __init__(self, potato):
        self.potato = potato

    @property
    def potato(self):
        return self.two + self.one

    @potato.setter
    def potato(self, potato):
        self.apple = 1

    def print_attributes(self):
        print(self.potato)
        print(self.apple)


class One:

    __slots__ = ["one"]

    def __init__(self, one):
        self.one = one


class Two:

    def __init__(self, two):
        self.two = two

a = One(1)
b = Two(2)

print(sys.getsizeof(a))
print(sys.getsizeof(b))
