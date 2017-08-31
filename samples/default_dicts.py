"""
This default dict thing allows you to set up a dictionary without having to
worry about what is beneath it.
"""
from collections import defaultdict, OrderedDict

"""
Default is list.
"""
potato = defaultdict(list)
potato["potato"].append(1)


"""
Default is a defaultdict of ints.
"""
apple = defaultdict(lambda: defaultdict(lambda: 0))
apple["apple"]["potato"] += 1
apple["apple"]["potatosalad"] += 1


"""
Defaults as class instances.
"""
class Car:

    def __init__(self, color, kind):
        self.color = color
        self.kind = kind


def test_default_dict():
    x = [("chevy", ("silverado", (("color", "red"), ("kind", "truck"))))]
    cars = defaultdict(lambda: defaultdict(lambda: Car("white", "coupe")))
    for k, v in x:
        cars[k][v[0]] = Car(v[1][0][1], v[1][1][1])
    assert cars["chevy"]["silverado"].kind == "truck"

    beatles = defaultdict(list)
    beatles["john"] = 1
    beatles["paul"] = [1, 2, 3, 4]
    assert beatles
