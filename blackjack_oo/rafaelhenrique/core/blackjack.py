# -*- coding: utf-8 -*-
from decimal import Decimal
from random import shuffle



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

    # def hit(self):
    #     """
    #     This function get one card of an deck and
    #     remove this card from original deck
    #     """
    #     card = self.deck.pop(0)
    #     self.hand.append(card)
    #     return card

    def show_points(self):
        """Calculate and return points from actual hand"""
        points = 0
        for card in self.hand:
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
