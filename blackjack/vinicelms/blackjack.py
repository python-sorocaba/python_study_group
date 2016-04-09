# -*- coding: utf-8 -*-

"""
Doctest deck

>>> deck = create_deck()  # Test create_deck
>>> len(deck)
52
>>> ten_firsts = deck[0:10]  # Test shuffle
>>> shuffle(deck)
>>> deck[0:10] != ten_firsts
True
>>> cards_in_deck = len(deck)
>>> card_for_player = get_card_from_deck(deck)
>>> card_for_player not in deck  # Test if the cards are no longer in deck
True
>>> cards_in_deck -1 == len(deck)
True
>>> player_cards = deal_cards(deck)
>>> len(player_cards)
2
>>> cards_value = cards_value()
>>> sum(cards_value.values())
85
"""
import random
from random import shuffle

player_money = 2000

def create_deck():
    """This function create an deck with 52 cards"""
    numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10"]
    letters = ["A", "Q", "J", "K"]
    suits = ["♣", "♦", "♥", "♠"]

    deck = []
    for suit in suits:
        for number in numbers:
            deck.append("{}{}".format(number, suit))
        for letter in letters:
            deck.append("{}{}".format(letter, suit))

    return deck

def cards_value():
    """Create dictionary with value of cards"""
    numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10"]
    letters = ["A", "Q", "J", "K"]
    value_of_cards = {}

    for number in numbers:
        value_of_cards[number] = int(number)

    for letter in letters:
        if letter == "A":
            value_of_cards[letter] = 1
        else:
            value_of_cards[letter] = 10

    return value_of_cards

def show_points(player_hand):
    print("Pontos no jogo: {}".format(get_points(player_hand)))

def get_points(player_hand):
    value_of_cards = cards_value()
    points = 0
    for card in player_hand:
        points = points + value_of_cards[card[:-3]]
    return points

def deal_cards(deck):
    """2 cards is returned to player from deck"""
    player_cards = []
    for i in range(0, 2):
        player_cards.append(get_card_from_deck(deck))
    return player_cards

def get_card_from_deck(deck):
    """Player get card from deck: Card is removed from deck and returned
        to player"""
    card_for_player = deck[0]
    deck.pop(0)
    return card_for_player


def show_hand(player_hand):
    print("O jogador tem {} cartas: {}".format(len(player_hand), ", ".join(player_hand)))

def surrender(player_hand):
    show_points(player_hand)
    exit(0)

def show_money():
    print("Saldo: {}".format(player_money))

def debit_money(debit_value):
    global player_money
    if debit_value <= player_money:
        player_money = player_money - debit_value
    else:
        raise ValueError("O valor solicitado é maior do que seu saldo!")


if __name__ == "__main__":
    deck = create_deck()
    shuffle(deck)
    player_hand = deal_cards(deck)
    show_hand(player_hand)
    show_money()
    try:
        debit_money(1990)
        show_money()
    except ValueError as e:
        print("\n\n{}\n\n".format(e))
        show_money()
