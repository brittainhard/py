from cards import *
from card_factory import *
from suits import *
from init import *



def test_card_factory():
    """The book provides for a number of different functions for getting card
    bappings. This test makes sure they all work. The same basic formula is
    this: they take a rank and suit, and use the .get method in a dictionary to
    give back the cards. For all of these functions, the default return from
    .get is a NumberCard instance."""
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


def test_card_factory_class():
    factory = CardFactory()
    deck = factory.get_deck()
    assert len(deck) == 52


def test_superclass_type():
    assert str(X.__class__) == "<class 'type'>"


def test_superclass_base():
    assert str(X.__class__.__base__) == "<class 'object'>"


def test_assert_no_init_method():
    r = Rectangle()
    r.length, r.width = 13, 8
    assert r.area() == 104
