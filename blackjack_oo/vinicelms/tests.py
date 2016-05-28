import unittest
from blackjack import Deck

class TestDeck(unittest.TestCase):
    def setUp(self):
        self.numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10"]
        self.letters = ["A", "Q", "J", "K"]
        self.suits = ["♣", "♦", "♥", "♠"]
        self.deck = Deck().deck

    def test_create_deck(self):
        deck_size = len(self.deck)
        self.assertEqual(deck_size, 52)

    def test_repeated_card_deck(self):
        card_dict_count = {}

        for card in self.deck:
            if card not in card_dict_count:
                card_dict_count[card] = 1
            else:
                card_dict_count[card] += 1

        for card_quantity in card_dict_count.values():
            self.assertFalse(card_quantity > 1)

    def test_card_have_suit(self):
        for card in self.deck:
            self.assertTrue(card[-1::] in self.suits)
