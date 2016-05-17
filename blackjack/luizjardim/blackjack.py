# -*- coding: utf-8 -*-

import random
import sys

def create_deck():
    faces = ["A", "2", "3", "4", "5", "6",
               "7", "8", "9", "10", "Q", "J",
               "K"]
    suits = ["♣", "♦", "♥", "♠"]
    deck = [face+suit for face in faces for suit in suits]
    return deck


def initial_round(hand):
    hit_card(deck, hand)
    hit_card(deck, hand)
    return hand

def shuffle_deck(deck):
    print('The deck was shuffle')
    return random.shuffle(deck)


def hit_card(deck, hand):
    card_hit = deck.pop(0)
    hand.append(card_hit)
    return card_hit


def show_hand(hand):
    return print(hand)


def show_points(hand):
    points = []
    for point in hand:
        if point[:-1] in 'QJK':
            points.append(10)
        elif point[:-1] == 'A':
            points.append(1)
        else:
            points.append(int(point[:-1]))
    total = sum(points)
    return total


def surrender():
    return sys.exit()


def show_money(money):
    return print("You own R$: {}".format(money))


def bet(money):

    choice = int(input('''Choose an option:
            (1) For bet $ 1
            (5) For bet $ 5
            (25) For bet $ 25
            (100) For bet $ 100
            Your option here: '''))

    if choice == 1:
        times = int(input("How many times do you want to bet $ 1 ? \n"))
        if money < choice*times:
            print("You don't have balance for this bet. Try again")
            pass

        money -= choice*times


    elif choice == 5:
        times = int(input("How many times do you want to bet $ 5 ? \n"))
        if money < choice*times:
            print("You don't have balance for this bet. Try again")
            pass
        money -= choice*times


    elif choice == 25:
        times = int(input("How many times do you want to bet $ 25 ? \n"))
        if money < choice*times:
            print("You don't have balance for this bet. Try again")
            pass
        money -= choice*times



    elif choice == 100:
        times = int(input("How many times do you want to bet $ 100 ? \n"))
        if money < choice*times:
            print("You don't have balance for this bet. Try again")
            pass
        money -= choice*times

    else:
        print("There's no such option")

    return money




if __name__ == "__main__":
    print('<'*20 + " Welcome to the blackjack table " + '>'*20)

    computer_hand = []
    player_hand = []

    balance = 2000

    deck = create_deck() # Create deck
    shuffle_deck(deck) # Shuffle deck

    player  = initial_round(player_hand)
    print("This are your initial cards {}".format(player))
    computer = initial_round(computer_hand)
    print("The computer cards {}".format(computer))



    while True:
        choice = int(input("\n" +
                           ">"*20 +
                           "\nWhat do you want now?"
                           "\n(1) Bet"
                           "\n(2) Hit a card"
                           "\n(3) Surrender"
                           "\nYour option here: "))

        if choice == 1:
            print('\n')
            bet(balance)
            show_money(balance)
            show_hand(player_hand)
            print("Your points: {}".format(show_points(player_hand)))

        elif choice == 2:
            print('\n')
            hit_card(deck, player_hand)
            hit_card(deck, computer_hand)

            if show_points(player_hand) > 21:
                print("You Lose")
                print("Your points: {}".format(show_points(player_hand)))
                print("Computer points: {}".format(show_points(computer_hand)))
                print("This is your hand")
                show_hand(player_hand)
                print("This is the computer hand")
                show_hand(computer_hand)
                print("See you next time")
                surrender()

            elif show_points(player_hand) == 21:
                print("You win!! Congratulations")
                print("Your points: {}".format(show_points(player_hand)))
                print("Computer points: {}".format(show_points(computer_hand)))
                print("This is your hand")
                show_hand(player_hand)
                print("This is the computer hand")
                show_hand(computer_hand)
                print("See you next time")
                surrender()

            elif show_points(computer_hand) > 21:
                print("Computer loose. You Win!! Congratulations")
                print("Your points: {}".format(show_points(player_hand)))
                print("Computer points: {}".format(show_points(computer_hand)))
                print("This is your hand")
                show_hand(player_hand)
                print("This is the computer hand")
                show_hand(computer_hand)
                print("See you next time")
                surrender()

            elif show_points(computer_hand) == 21:
                print("Computer Win")
                print("Your points: {}".format(show_points(player_hand)))
                print("Computer points: {}".format(show_points(computer_hand)))
                print("This is your hand")
                show_hand(player_hand)
                print("This is the computer hand")
                show_hand(computer_hand)
                print("See you next time")
                surrender()

            else:
                print("Keep going")
                print("Your points: {}".format(show_points(player_hand)))
                print("Computer points: {}".format(show_points(computer_hand)))
                print("This is your hand")
                show_hand(player_hand)
                print("This is the computer hand")
                show_hand(computer_hand)

        elif choice == 3:
            print('\n')
            show_points(player_hand)
            print('\nThanks for playing')
            surrender()

        else:
            print("There's no such option. Try again")