# -*- coding: utf-8 -*-
from decimal import Decimal


class Blackjack:
    numbers = ["A", "2", "3", "4", "5", "6",
               "7", "8", "9", "10", "Q", "J",
               "K"]
    suits = ["♣", "♦", "♥", "♠"]

    def __init__(self):
        self.deck = ["{}{}".format(number, suit)
                     for suit in self.suits
                     for number in self.numbers]
        self.money = Decimal('2000.0')

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
