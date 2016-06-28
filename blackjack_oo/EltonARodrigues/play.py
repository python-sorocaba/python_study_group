# -*- coding: utf-8 -*-

from core.player import Player
from core.blackjack import Blackjack
from core.frenchdeck.py import Frenchdeck

if __name__ == '__main__':

	player = Player("Rafael", 2000.0)
	dealer = Player("Dealer", 0)
	deck = FrenchDeck()
	game = Blackjack(dealer, player, deck)