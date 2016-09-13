from decimal import Decimal
from .deck import Card

class Hand:
    def __init__(self, cards=None):
        if not cards:
            self.cards = list()
        else:
            self.cards = cards

    def append(self, card):
        if isinstance(card, Card):
            self.cards.append(card)
        else:
           raise ValueError("Value must be a Card!")

class Player:
    def __init__(self, name, money='2000.0'):
        self.name = name
        self.hand = Hand()
        self.money = Decimal(money)

    def hit(self, deck):
        card = deck.pop(0)
        self.hand.append(card)

    @property
    def points(self):
        points = 0
        for card in self.hand.cards:
            points += card.card_value()
        return points