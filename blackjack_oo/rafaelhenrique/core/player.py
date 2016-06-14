"""
Doctest for Player

>>> from core.frenchdeck import Card
>>> player = Player("Rafael", 2000.0)
>>> card = Card('11', 'spades')
>>> player.hand.append(card)
>>> player.points
11
>>> print(player.hand)
1 card: 11spades
>>> card = Card('A', 'spades')
>>> player.hand.append(card)
>>> print(player.hand)
2 cards: 11spades,Aspades
>>> player.points
12
"""

from decimal import Decimal

class Hand:
    def __init__(self, cards=None):
        if not cards:
            self._cards = list()
        else:
            self._cards = cards

    def append(self, item):
        self._cards.append(item)

    def __str__(self):
        """Show all cards on hand"""
        qty_cards = len(self._cards)
        if qty_cards >= 2:
            cards = ", ".join(self._cards)
            msg = "{} cards: {}".format(qty_cards, cards)
        elif qty_cards == 1:
            cards = ", ".join(self._cards)
            msg = "{} card: {}".format(qty_cards, cards)
        else:
            msg = "You dont have cards on hand!"
        return msg

    def __repr__(self):
        return "Hand(cards={0!r})".format(self._cards)


class Player:
    def __init__(self, name, money='2000.0'):
        self.name = name
        self.money = Decimal(money)
        self.hand = Hand()

    def hit(self, deck):
        """
        This function get one card of an deck and
        remove this card from original deck
        """
        card = deck.pop(0)
        self.hand = card


