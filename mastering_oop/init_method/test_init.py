from cards import *
from card_factory import *
from suits import *
from init import *


def test_card_factory():
    number_card = card(3, Spade)
    ace_card = card(1, Heart)
    jack = card(11, Club)
    queen = card(12, Diamond)
    king = card(13, Spade)
    assert type(number_card) == NumberCard
    assert type(ace_card) == AceCard
    assert type(jack) == FaceCard
    assert type(queen) == FaceCard
    assert type(king) == FaceCard


def test_card_better_elif():
    number_card = card_better_elif(3, Spade)
    ace_card = card_better_elif(1, Heart)
    jack = card_better_elif(11, Club)
    queen = card_better_elif(12, Diamond)
    king = card_better_elif(13, Spade)
    assert type(number_card) == NumberCard
    assert type(ace_card) == AceCard
    assert type(jack) == FaceCard
    assert type(queen) == FaceCard
    assert type(king) == FaceCard


def test_card_mapping():
    number_card = card_mapping(3, Spade)
    ace_card = card_mapping(1, Heart)
    jack = card_mapping(11, Club)
    queen = card_mapping(12, Diamond)
    king = card_mapping(13, Spade)
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
