class A:

    def spam(self):
        print("A.Spam")


class B(A):
    """
    Just an example on how to call the parent.
    """

    def spam(self):
        print("B.Spam")
        super().spam()


b = B()


class C:

    def __init__(self):
        self.x = 0

    def print_x(self):
        print(self.x)

    def potato(self):
        print("Potato")


class D(C):
    """
    Not adding super() will cause it to fail when you try to run the print_x
    function.

    The potato function works fine without the super init.
    """

    def __init__(self):
        super().__init__()
        self.y = 1


d = D()
