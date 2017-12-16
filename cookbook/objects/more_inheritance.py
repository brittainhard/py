class Base:

    def __init__(self):
        print("Base init")


class A(Base):

    def __init__(self):
        super().__init__()
        print("A init")


class B(Base):

    def __init__(self):
        super().__init__()
        print("B init")


class C(A, B):

    def __init__(self):
        super().__init__()
        print("C init")


c = C()
