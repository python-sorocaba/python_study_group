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
import os
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
    separator = ", "
    cards = separator.join(hand)
    print (cards)


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
   my_cards, computer_cards = [hit(deck)],[hit(deck)]
   to_bet = True

   while to_bet:
       is_ready = input("Do you want to bet? [y/n] ")

       if is_ready in ("y", "Y"):
           to_bet = True
       elif is_ready in ("n", "N"):
           to_bet = False
           continue
       else:
           print("Y or N")
           continue
        
       os.system('cls' if os.name == 'nt' else 'clear')
       
       my_cards += [hit(deck)]
       computer_cards += [hit(deck)]
       print("\n")
       print("Your Cards: {}".format(my_cards))
       print("Computer Cards: {}".format(computer_cards))
       print("\n")

   my_points = show_points(my_cards)
   computer_points = show_points(computer_cards)
   os.system('cls' if os.name == 'nt' else 'clear')
<<<<<<< HEAD
   
   if my_points > 21:
        print("-----------------------") 
        print("YOU LOOSE")
        print("-----------------------")
   elif computer_points > 21:
        print("-----------------------")
        print("YOU WIN")
        print("-----------------------")
   elif my_points < computer_points:
        print("-----------------------")
        print("YOU LOOSE")
        print("-----------------------")
   elif my_points > computer_points:
        print("-----------------------")
        print("YOU WIN")
        print("-----------------------")
   elif my_points == computer_points:
        print("-----------------------")
        print("TIED THE GAME")
        print("-----------------------\n")
  
=======
>>>>>>> 3ea7f6b754a32434aeebe330db117e357c15078a
   print("\n")
   print("Your Points: {}".format(my_points), " -> {}".format(my_cards),("\n"))
   print("Computer Points: {}".format(computer_points), " -> {}".format(computer_cards),("\n"))