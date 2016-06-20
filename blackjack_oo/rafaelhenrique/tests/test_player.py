import unittest
from core.player import Player
from core.frenchdeck import Card


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player('Rafael', 2000.0)
        self.card_one = Card('Q', 'spades')
        self.card_two = Card('A', 'spades')

    def test_repr(self):
        expected = ("Player(name='Rafael', money=Decimal('2000'), "
                    "hand=Hand(cards=[]))")
        self.assertEqual(repr(self.player), expected)

    def test_points(self):
        self.player.hand.append(self.card_one)
        self.assertEqual(self.player.points, 10)

    def test_one_card_on_hand_append(self):
        self.player.hand.append(self.card_one)
        self.assertEqual(str(self.player.hand), "1 card: Q spades")

    def test_two_cards_on_hand_append(self):
        self.player.hand.append(self.card_one)
        self.player.hand.append(self.card_two)
        self.assertEqual(str(self.player.hand), "2 cards: Q spades,A spades")

    def test_show_money(self):
        self.assertEqual(str(self.player.money), "2000")

    def test_bet(self):
        coin = self.player.bet(100)
        self.assertEqual(self.player.money, 1900.0)
        self.assertEqual(coin, 100)

    def test_bet_invalid_coin(self):
        with self.assertRaises(ValueError):
            self.player.bet(200)
