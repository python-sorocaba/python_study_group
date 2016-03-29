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
"""
import random


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


def shuffle(deck):
    """This function shuffle one deck"""
    random.shuffle(deck)


def hit(deck):
    card = random.choice(deck)
    deck.remove(card)    
    return card

if __name__ == "__main__":
    deck = create_deck()
    shuffle(deck)
    hit(deck)
