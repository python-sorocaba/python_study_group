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
>>> show_hand(hand)
3 cards: A♣, 2♣, 3♣
>>> hand = ["A♣"]
>>> show_hand(hand)
1 card: A♣
"""
import random
from random import shuffle
# from random import shuffle as shuffle_deck


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
    return deck.pop(0)


def show_hand(hand):
    qty_cards = len(hand)
    if qty_cards >= 2:
        msg = "{} cards: {}"
    else:
        msg = "{} card: {}"
    separator = ", "
    cards = separator.join(hand)
    print(msg.format(qty_cards, cards))

if __name__ == "__main__":
    deck = create_deck()
    shuffle(deck)
    print(deck)
    hand = [hit(deck) for _ in range(2)]
    show_hand(hand)
    print("*"*20)
