from functools import partial

"""
Some notes about how partial functions work.

They are lazy evaluation. 
"""
class Potato:

    def __init__(self, a, b):
        self.a = a
        self.b = b


def test_partials():
    part_class = partial(Potato, 1, 2)
    assert part_class().a == 1
    assert part_class().b == 2
