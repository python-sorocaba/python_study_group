import unittest
from core.player import Player
from core.frenchdeck import FrenchDeck
from core.blackjack import Blackjack


class TestBlackjack(unittest.TestCase):

    def setUp(self):
        self.deck = FrenchDeck()
        self.player = Player("Rafael", 2000.0)
        self.dealer = Player("Dealer", 0)
        self.game = Blackjack(self.dealer, self.player, self.deck)

    def test_repr(self):
        expected = ("Blackjack(dealer='Dealer', player='Rafael')")
        self.assertEqual(repr(self.game), expected)

    def test_start(self):
        self.game.start()
        self.assertEqual(len(self.dealer.hand), 2)
