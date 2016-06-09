import unittest
from core.player import Player
from core.frenchdeck import Card


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player('Rafael')
        self.card_one = Card('11', 'spades')
        self.card_two = Card('A', 'spades')

    def test_repr(self):
        self.assertEqual(repr(self.player), "Player(name='Rafael')")

    def test_points(self):
        self.player.hand.append(self.card_one)
        self.assertEqual(self.player.points, 11)

    def test_one_card_on_hand_append(self):
        self.player.hand.append(self.card_one)
        self.assertEqual(str(self.player.hand), "1 card: 11spades")

    def test_two_cards_on_hand_append(self):
        self.player.hand.append(self.card_one)
        self.player.hand.append(self.card_two)
        self.assertEqual(str(self.player.hand), "2 cards: 11spades,Aspades")
