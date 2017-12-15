class Foo:
    """
    Python is a consenting adult's language. No such thing as private and public
    methods.

    If this leads me away from doing this very natural thing, then its
    definitely to be stopped. I know you didn't need to need. Needing. Needling

    Fiddling.
    """

    def __init__(self):
        self._internal = 0
        self.public = 1

    def public_method(self):
        pass

    def _internal_method(self):
        pass


class A:
    """
    Not done with this, not yet.

    With these, when you add the __, it changes the name of the thing to the
    name of the class, plus the double underscore `_A__priavte_method.`

    It's encapsulation by confusion.
    """

    def __init__(self):
        self.__private = 0

    def __private_method(self):
        print("This is A's private method.")

    def public_method(self):
        self.__private_method()


class B(A):
    
    def __init__(self):
        super().__init__()
        self.__private = 1

    # Does not override B.__private_method
    def __private_method(self):
        print("This is B's private method.")


a = B()
print(a._B__private)
a._A__private_method()
a._B__private_method()
