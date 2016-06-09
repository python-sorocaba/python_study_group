"""
Doctest for Player

>>> from core.frenchdeck import Card
>>> player = Player("Rafael")
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


class Hand:

    def __init__(self):
        self._hand = []

    def append(self, item):
        self._hand.append(item)

    def __str__(self):
        cards_quantity = len(self._hand)
        if cards_quantity == 0:
            return "You dont have cards on hand!"
        else:
            cards = ["{}{}".format(card.rank, card.suit)
                     for card in self._hand]
            cards = ",".join(cards)
            if cards_quantity > 1:
                message = "{} cards: {}".format(cards_quantity, cards)
            else:
                message = "{} card: {}".format(cards_quantity, cards)
        return message

    def __getitem__(self, position):
        return self._hand[position]


class Player:

    def __init__(self, name):
        self.name = name
        self.hand = Hand()

    def __repr__(self):
        return "Player(name={!r})".format(self.name)

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
