"""
A hash reduces a complex value to a small integer value. The hash method is
used to create a small integer key that works with collections such as set,
frozenset, and dict.

A hash value can be used to rapidly locate an object in a collection. The object
needs to be an immutable object.

Immutable objects don't change their state.
"""
class Potato:
    pass


class PotatoSack(Potato):
    pass
