"""
Advanced Circle Alanytics Company
"""
import math


class Circle:
    """Advanced circle analytics toolkit."""

    version = "0.1"

    def __init__(self, radius):
        """
        Init is not a constructor.
        """
        self.radius = radius

    @classmethod
    def from_bbd(cls, bbd):
        """THIS is a constructor. It takes the class, and you combine the class
        with the arguments. It would be similar if you just grabbed the Circle
        class and then passed this as an argument.

        Just API stuff. Seems like an insignifiant thing.
        """
        radius = bbd / 2.0 / math.sqrt(2.0)
        return cls(radius)

    @staticmethod
    def angle_to_grade(angle):
        """Since classes are basically namespaces, why not juse go ahead and use
        the classes as namespaces?"""
        return math.tan(math.raidus(angle)) * 100

    def area(self):
        return math.pi * self.radius ** 2.0

    def perimeter(self):
        return 2.0 * math.pi * self.radius


class Tire(Circle):
    """Tires with a corrected perimeter weird use of it. Not advisable that they
    do this, but whatever.
    """

    def perimiter(self):
        # Allow this?
        return Circle.perimiter(self) * 1.2


def test_instantiate():
    a = Circle.from_bbd(1)
