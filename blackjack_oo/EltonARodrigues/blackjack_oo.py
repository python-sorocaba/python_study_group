# -*- coding: utf-8 -*-

from decimal import Decimal
from random import shuffle

class BlackJack(object):

    numbers = ["A", "2", "3", "4", "5", "6",
               "7", "8", "9", "10", "Q", "J",
               "K"]
    suits = ["♣", "♦", "♥", "♠"]

    def __init__(self):
        self.deck = ["{}{}".format(number, suit)
                     for suit in self.suits
                     for number in self.numbers]
        self.money = Decimal('2000.0')

    def show_points(self):
        """Calculate and return points from actual hand"""
        points = 0
        Play = Player()
        for card in Play.hand:
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

class Player(object):

    def __init__(self, money='2000.0'):
        self.money = Decimal(money)
        self._hand = []

    @property
    def hand(self):
        return self._hand

    @hand.setter
    def hand(self, value):
        if isinstance(value, str):
            self._hand.append(value)
        elif isinstance(value, list):
            self._hand += value
        else:
            raise ValueError('This value should be a string or list!')

    def show_hand(self):
        """Show all cards on hand"""
        qty_cards = len(self.hand)
        if qty_cards >= 2:
            cards = ", ".join(self.hand)
            msg = "{} cards: {}".format(qty_cards, cards)
        elif qty_cards == 1:
	        cards = ", ".join(self.hand)
	        msg = "{} card: {}".format(qty_cards, cards)
        else:
	        msg = "You dont have cards on hand!"
        print(msg)

    def hit(self, deck):
        """
        This function get one card of an deck and
        remove this card from original deck
        """
        card = deck.pop(0)
        self.hand = card


if __name__ == "__main__":
    P = Player()
    B = BlackJack()

    print(B.deck)
    
    P.show_hand()
    total_bet = [B.bet(100) for _ in range(4)]
    print("My coins: {}".format(total_bet))
    try:
        B.bet(30)
    except Exception as e:
        print(e)
    B.show_money()
    print("*"*20)
    # Add one more card on hand to verify
    # how surrender function works
    P.hand.append(P.hit(B.deck))
    B.surrender()
