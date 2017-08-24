from cards import *
from card_factory import *
from suits import *
from init import *



def test_card_factory():
    for x in factory_functions:
        number_card = x(3, Spade)
        ace_card = x(1, Heart)
        jack = x(11, Club)
        queen = x(12, Diamond)
        king = x(13, Spade)
        assert type(number_card) == NumberCard
        assert type(ace_card) == AceCard
        assert type(jack) == FaceCard
        assert type(queen) == FaceCard
        assert type(king) == FaceCard


def test_superclass_type():
    assert str(X.__class__) == "<class 'type'>"


def test_superclass_base():
    assert str(X.__class__.__base__) == "<class 'object'>"


def test_assert_no_init_method():
    r = Rectangle()
    r.length, r.width = 13, 8
    assert r.area() == 104
