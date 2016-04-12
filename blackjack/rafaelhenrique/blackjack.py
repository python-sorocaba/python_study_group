# -*- coding: utf-8 -*-
"""
Doctest do baralho

>>> deck = create_deck()  # Test create_deck
>>> len(deck)
52
>>> ten_firsts = deck[0:10]  # Test shuffle
>>> shuffle(deck)
>>> deck[0:10] != ten_firsts
True
>>> card = hit(deck)  # Test hit
>>> len(deck) == 51
True
>>> fake_deck = create_deck()   # Test hit 2
>>> card1, card2, card3 = hit(deck), hit(deck), hit(deck)
>>> hand = [card1, card2, card3]
>>> is_str = [isinstance(card, str) for card in hand]
>>> is_str == [True, True, True]
True
>>> all(is_str)
True
>>> in_fake_deck = [True for card in hand if card in fake_deck]
>>> in_fake_deck == [True, True, True]
True
>>> all(in_fake_deck)
True
>>> not_in_deck = [True for card in hand if card not in deck]
>>> all(not_in_deck)
True
>>> hand = ["A♣", "2♣", "3♣"]
>>> show_hand(hand)  # Test show_hand
3 cards: A♣, 2♣, 3♣
>>> hand = ["A♣"]
>>> show_hand(hand)  # Test show_hand 2
1 card: A♣
>>> show_points(hand)  # Test show_points
Points: 1
>>> hand = ["A♣", "2♣", "3♣"]
>>> show_points(hand)  # Test show_points 2
Points: 6
>>> hand = ["J♣", "K♣", "3♣"]
>>> show_points(hand)  # Test show_points 3
Points: 23
>>> show_money()  # Test show_money
Money: R$ 2000.00
>>> bet(100)  # Test bet
100
>>> show_money()
Money: R$ 1900.00
>>> # bet(30)  # Test bet raise exception
>>> # surrender()  # Test surrender raise
"""
from decimal import Decimal
from random import shuffle


def create_deck():
    """This function create an deck with 52 cards"""
    numbers = ["A", "2", "3", "4", "5", "6",
               "7", "8", "9", "10", "Q", "J",
               "K"]
    suits = ["♣", "♦", "♥", "♠"]

    deck = []
    for suit in suits:
        for number in numbers:
            deck.append("{}{}".format(number, suit))
    return deck


def hit(deck):
    """
    This function get one card of an deck and
    remove this card from original deck
    """
    return deck.pop(0)


def show_hand(hand):
    """Show all cards on hand"""
    qty_cards = len(hand)
    if qty_cards >= 2:
        msg = "{} cards: {}"
    else:
        msg = "{} card: {}"
    separator = ", "
    cards = separator.join(hand)
    print(msg.format(qty_cards, cards))


def show_points(hand):
    """Calculate and return points from actual hand"""
    points = 0
    for card in hand:
        # solution with regex:
        # pattern = re.compile("\d+")
        # match = pattern.match(card)
        number = card[:-1]

        if number == "A":
            points += 1
        elif number in ("K", "J", "Q"):
            points += 10
        else:
            number = int(number)
            points += number
    print("Points: {}".format(points))


def show_money():
    print("Money: R$ {:.2f}".format(MONEY))


def bet(coin):
    global MONEY
    if coin not in (1, 5, 25, 100):
        raise Exception("Invalid coin to bet")
    if MONEY >= coin:
        MONEY -= coin
        return coin
    return None


def surrender():
    print("Finish with...")
    show_points(HAND)
    raise SystemExit

MONEY = Decimal('2000.0')
DECK = create_deck()
shuffle(DECK)
HAND = [hit(DECK) for _ in range(3)]

if __name__ == "__main__":
    print(DECK)
    show_hand(HAND)
    show_points(HAND)
    total_bet = [bet(100) for _ in range(4)]
    print("My coins: {}".format(total_bet))
    try:
        bet(30)
    except Exception as e:
        print(e)
    show_money()
    print("*"*20)
    # Add one more card on hand to verify
    # how surrender function works
    HAND.append(hit(DECK))
    surrender()
