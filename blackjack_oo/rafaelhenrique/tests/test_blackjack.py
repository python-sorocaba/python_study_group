import unittest
from core.player import Player
from core.frenchdeck import FrenchDeck
from core.blackjack import Blackjack
from core.frenchdeck import Card


class TestBlackjack(unittest.TestCase):

    def setUp(self):
        self.deck = FrenchDeck()
        self.player = Player("Rafael", 2000.0)
        self.dealer = Player("Dealer", 0)
        self.game = Blackjack(self.dealer, self.player, self.deck)

    def test_repr(self):
        expected = (
            "Blackjack(dealer='Dealer', player='Rafael', current_bet=0)")
        self.assertEqual(repr(self.game), expected)

    def test_start(self):
        self.game.start()
        self.assertEqual(len(self.dealer.hand), 2)

    def test_header(self):
        self.dealer.hand.append(Card('Q', 'spades'))
        self.dealer.hand.append(Card('Q', 'diamonds'))
        self.dealer.hand.append(Card('Q', 'clubs'))

        expected = (
            'BLACKJACK -> Saldo: 2000 | Aposta Atual: 0 | Seus pontos: 0\n'
            'Dealer hand -> 3 cards: Q spades,Q diamonds,HIDE CARD\n'
            'Player hand -> You dont have cards on hand!\n')
        self.assertEqual(self.game.header, expected)
