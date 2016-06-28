# -*- coding: utf-8 -*-
"""
Doctest for Blackjack
>>> from core.frenchdeck import FrenchDeck
>>> from core.blackjack import Blackjack
>>> from core.player import Player
>>> deck = FrenchDeck()
>>> player = Player("Rafael", 2000.0)
>>> dealer = Player("Dealer", 0)
>>> game = Blackjack(dealer, player, deck)
>>> game.start()
>>> len(dealer.hand) == 2
True
"""

from decimal import Decimal
from random import shuffle



class Blackjack:
    numbers = ["A", "2", "3", "4", "5", "6",
               "7", "8", "9", "10", "Q", "J",
               "K"]
    suits = ["♣", "♦", "♥", "♠"]

    def __init__(self,dealer,player,deck):
        self.dealer = dealer
        self.player = player
        self.deck = deck

    # def hit(self):
    #     """
    #     This function get one card of an deck and
    #     remove this card from original deck
    #     """
    #     card = self.deck.pop(0)
    #     self.hand.append(card)
    #     return card



    def show_money(self):
        print("Money: R$ {:.2f}".format(self.money))

    def bet(self, coin):
        if coin not in (1, 5, 25, 100):
            raise Exception("Invalid coin to bet")
        if self.money >= coin:
            self.money -= coin
            return coin
        return None

    def surrender(self):
        print("Finish with...")
        self.show_points()
        raise SystemExit

    def start(self):
        pass


if __name__ == "__main__":
    player1 = Player()
    print(player1.money)
    # import ipdb; ipdb.set_trace()
    player1.show_hand()

    # game = Blackjack()
    # print(game.deck)
    # game.show_hand()
    # game.show_points()
    # total_bet = [game.bet(100) for _ in range(4)]
    # print("My coins: {}".format(total_bet))
    # try:
    #     game.bet(30)
    # except Exception as e:
    #     print(e)
    # game.show_money()
    # print("*"*20)
    # # Add one more card on hand to verify
    # # how surrender function works
    # game.hit()
    # game.surrender()
