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
1
>>> hand = ["A♣", "2♣", "3♣"]
>>> show_points(hand)  # Test show_points 2
6
>>> hand = ["J♣", "K♣", "3♣"]
>>> show_points(hand)  # Test show_points 3
23
"""
import re
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
        pattern = re.compile("[2-9]")
        match = pattern.match(card)

        if card.find("A") == 0:
            points += 1
        elif match:
            number = int(match.group(0))
            points += number
        elif re.search("[K,J,Q]", card):
            points += 10

    return points

if __name__ == "__main__":
    deck = create_deck()
    shuffle(deck)
    print(deck)
    hand = [hit(deck) for _ in range(3)]
    show_hand(hand)
    points = show_points(hand)
    print("Points: {}".format(points))
    print("*"*20)
