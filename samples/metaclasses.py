class InterfaceMeta(type):

    def __new__(cls, name, bases, attrs):
        if "salad" not in attrs:
            attrs["salad"] = "salad"
        return super().__new__(cls, name, bases, attrs)


class Interface(metaclass=InterfaceMeta):

    def __init__(self, potato):
        self.potato = potato


def test_meta():
    a = Interface("1")
    assert a.salad == "salad"
