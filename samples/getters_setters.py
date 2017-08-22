class Circle(object):

    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self.diameter / 2.0

    @radius.setter
    def radius(self, radius):
        self.diameter = radius * 2.0


def test_circle():
    a = Circle(2)
    assert a.radius == 2.0
    assert a.diameter == 4.0
