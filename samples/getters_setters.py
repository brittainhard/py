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
    circ = Circle(2)
    assert circ.radius == 2.0
    assert circ.diameter == 4.0
