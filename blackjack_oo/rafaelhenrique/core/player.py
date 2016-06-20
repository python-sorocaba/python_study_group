"""
Doctest for Player

>>> from core.frenchdeck import Card
>>> player = Player("Rafael", 2000.0)
>>> card = Card('Q', 'spades')
>>> player.hand.append(card)
>>> player.points
10
>>> print(player.hand)
1 card: Q spades
>>> card = Card('A', 'spades')
>>> player.hand.append(card)
>>> print(player.hand)
2 cards: Q spades,A spades
>>> player.points
11
"""

from decimal import Decimal


class Hand:

    def __init__(self, cards=None):
        if not cards:
            self._cards = []
        else:
            self._cards = cards

    def append(self, item):
        self._cards.append(item)

    def __str__(self):
        cards_quantity = len(self._cards)
        if cards_quantity == 0:
            return "You dont have cards on hand!"
        else:
            cards = ["{} {}".format(card.rank, card.suit)
                     for card in self._cards]
            cards = ",".join(cards)
            if cards_quantity > 1:
                message = "{} cards: {}".format(cards_quantity, cards)
            else:
                message = "{} card: {}".format(cards_quantity, cards)
        return message

    def __getitem__(self, position):
        return self._cards[position]

    def __repr__(self):
        return "Hand(cards={!r})".format(self._cards)


class Player:

    def __init__(self, name, money):
        self.name = name
        self.hand = Hand()
        self.money = Decimal(money)

    def __repr__(self):
        return "Player(name={!r}, money={!r}, hand={!r})".format(
            self.name, self.money, self.hand)

    def bet(self, coin):
        if coin not in (1, 5, 25, 100):
            raise ValueError("Invalid coin to bet")
        if self.money >= coin:
            self.money -= coin
            return coin
        return None

    @property
    def points(self):
        """Calculate and return points from actual hand"""
        points = 0
        for card in self.hand:
            if card.rank == "A":
                points += 1
            elif card.rank in ("K", "J", "Q"):
                points += 10
            else:
                points += int(card.rank)
        return points
