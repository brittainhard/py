__all__ = ["X", "Rectangle"]


class X:
    pass


class Rectangle:
    """Optional attributes are a kind of subclass that is not declared as a
    proper subclass. I guess in the sense that all things in python are objets.
    If you have optional attributes, you may end up having to deal with a lot of
    contidtional problems, like if someone is checking to see if an attribute is
    set. In thise case, the init function would require arguments and so it
    would force you to declare them."""

    def area(self):
        return self.length * self.width
