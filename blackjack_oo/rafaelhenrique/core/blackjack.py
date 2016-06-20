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

from random import shuffle


class Blackjack:
    def __init__(self, dealer, player, deck):
        self.dealer = dealer
        self.player = player
        self.deck = deck
        self.started = False

    def __repr__(self):
        return "Blackjack(dealer={!r}, player={!r})".format(self.dealer.name,
                                                            self.player.name)

    def start(self):
        if self.started:
            return
        shuffle(self.deck)
        for _ in range(2):
            card = self.deck.pop(0)
            self.dealer.hand.append(card)
        self.started = True
