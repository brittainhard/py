from init_method import cards, card_factory, suits, init, alt_cards, deck, hands


def test_card_factory():
    """The book provides for a number of different functions for getting card
    bappings. This test makes sure they all work. The same basic formula is
    this: they take a rank and suit, and use the .get method in a dictionary to
    give back the cards. For all of these functions, the default return from
    .get is a NumberCard instance."""
    for x in card_factory.factory_functions:
        number_card = x(3, suits.Spade)
        ace_card = x(1, suits.Heart)
        jack = x(11, suits.Club)
        queen = x(12, suits.Diamond)
        king = x(13, suits.Spade)
        assert type(number_card) == cards.NumberCard
        assert type(ace_card) == cards.AceCard
        assert type(jack) == cards.FaceCard
        assert type(queen) == cards.FaceCard
        assert type(king) == cards.FaceCard


def test_card_factory_class():
    factory = card_factory.CardFactory()
    deck = factory.get_deck()
    assert len(deck) == 52


def test_superclass_type():
    assert str(init.X.__class__) == "<class 'type'>"


def test_superclass_base():
    assert str(init.X.__class__.__base__) == "<class 'object'>"


def test_assert_no_init_method():
    r = init.Rectangle()
    r.length, r.width = 13, 8
    assert r.area() == 104


def test_alt_cards():
    number_card = alt_cards.alt_card_factory(3, suits.Spade)
    ace_card = alt_cards.alt_card_factory(1, suits.Heart)
    jack = alt_cards.alt_card_factory(11, suits.Club)
    queen = alt_cards.alt_card_factory(12, suits.Diamond)
    king = alt_cards.alt_card_factory(13, suits.Spade)
    assert type(number_card) == alt_cards.NumberCard
    assert type(ace_card) == alt_cards.AceCard
    assert type(jack) == alt_cards.FaceCard
    assert type(queen) == alt_cards.FaceCard
    assert type(king) == alt_cards.FaceCard


def test_deck_one():
    current_deck = deck.Deck()
    assert len(current_deck) == 52
    current_deck.pop()
    assert len(current_deck) == 51


def test_list_deck():
    current_deck = deck.ListDeck()
    assert len(current_deck) == 52
    current_deck.pop()
    assert len(current_deck) == 51

def test_dealer_deck():
    current_deck = deck.DealerDeck(4)
    deck_length = len(current_deck)
    current_deck.pop()
    assert deck_length - 1 == len(current_deck)


def test_hands():
    current_deck = deck.ListDeck()
    hand1 = hands.BadHand(current_deck.pop())
    hand1.cards.append(current_deck.pop())
    assert len(hand1) == 1
    hand2 = hands.GoodHand(current_deck.pop(), current_deck.pop(), current_deck.pop())
    assert len(hand2) == 2
