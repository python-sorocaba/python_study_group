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
        self.current_bet = 0

    def __repr__(self):
        return "Blackjack(dealer={!r}, player={!r}, current_bet={!r})".format(
            self.dealer.name, self.player.name, self.current_bet)

    def start(self):
        if self.started:
            return
        shuffle(self.deck)
        for _ in range(2):
            card = self.deck.pop(0)
            self.dealer.hand.append(card)
        self.started = True

    @property
    def header(self):
        msg = ("BLACKJACK -> Saldo: {} | Aposta Atual: {} | Seus pontos: {}\n"
               "Dealer hand -> {}\n"
               "Player hand -> {}\n")

        dealer_hand = str(self.dealer.hand).split(',')[:-1] + ['HIDE CARD']
        dealer_hand = ",".join(dealer_hand)

        return msg.format(self.player.money,
                          self.current_bet,
                          self.player.points,
                          dealer_hand,
                          self.player.hand)
