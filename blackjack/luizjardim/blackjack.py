# -*- coding: utf-8 -*-

import random
import sys

def create_deck():
    '''Create a basic French deck with 52 cards'''
    faces = ["A", "2", "3", "4", "5", "6",
               "7", "8", "9", "10", "Q", "J",
               "K"]
    suits = ["♣", "♦", "♥", "♠"]
    deck = [face+suit for face in faces for suit in suits]
    return deck


def initial_round(hand):
    '''This function initialize the first round in the table'''
    hit_card(deck, hand)
    hit_card(deck, hand)
    return hand

def shuffle_deck(deck):
    '''This function shuffle the deck at the beginning of round'''
    print('The deck was shuffle')
    return random.shuffle(deck)


def hit_card(deck, hand):
    '''This function hit a card on the top of deck'''
    card_hit = deck.pop(0)
    hand.append(card_hit)
    return card_hit


def show_hand(hand):
    '''Show the cards in hand'''
    return print(hand)


def show_points(hand):
    '''Show the points of hand'''
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
    '''Finish the program and surrender'''
    return sys.exit()


def show_money(money):
    '''Show the balance of the player'''
    return print("You own R$: {}".format(money))


def bet(money):
    '''
    This function works to available bet on the game
    '''

    choice = int(input('''Choose an option:
            (1) For bet $ 1
            (5) For bet $ 5
            (25) For bet $ 25
            (100) For bet $ 100
            Your option here: '''))

    if choice in (1, 5, 25, 100):
        times = int(input("How many times do you want to bet $ {0} ? \n".format(choice)))
        if money < choice*times:
            print("You don't have balance for this bet. Try again")
            pass
        money -= choice*times

    else:
        print("There's no such option")

    return money

def msg_of_win(player, computer, msg):
    '''
    This function print a Winner message or a Lose message
    If the player was the winner or pc was the winner and vice and versa
    '''
    print(msg)
    print("Your points: {}".format(show_points(player)))
    print("Computer points: {}".format(show_points(computer)))
    print("This is your hand")
    show_hand(player)
    print("This is the computer hand")
    show_hand(computer)
    print("See you next time")
    surrender()

def keep_going(player, computer):
    '''This function keeps the game playing if
    the punctuation don't reach or exceed 21 '''
    print("Keep going")
    print("Your points: {}".format(show_points(player)))
    print("Computer points: {}".format(show_points(computer)))
    print("This is your hand")
    show_hand(player)
    print("This is the computer hand")
    show_hand(computer)


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
            show_money(bet(balance))
            show_hand(player_hand)
            print("Your points: {}".format(show_points(player_hand)))

        elif choice == 2:
            print('\n')
            hit_card(deck, player_hand)
            hit_card(deck, computer_hand)
            lose_msg = "You Lose"
            win_msg = "You win!! Congratulations"
            lose_pc_msg = "Computer loose. You Win!! Congratulations"
            win_pc_msg = "Computer Win"

            if show_points(player_hand) > 21:
                msg_of_win(player_hand, computer_hand, lose_msg)

            elif show_points(player_hand) == 21:
                msg_of_win(player_hand, computer_hand, win_msg)

            elif show_points(computer_hand) > 21:
                msg_of_win(player_hand, computer_hand, lose_pc_msg)

            elif show_points(computer_hand) == 21:
                msg_of_win(player_hand, computer_hand, win_pc_msg)

            else:
                keep_going(player_hand, computer_hand)

        elif choice == 3:
            print('\n')
            show_points(player_hand)
            print('\nThanks for playing')
            surrender()

        else:
            print("There's no such option. Try again")