# -*- coding: utf-8 -*-
import unittest
from blackjack_oo import BlackJack, Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player()

    def test_hand_property(self):
        self.player.hand = "A♣"
        self.assertEqual(self.player.hand, ["A♣"])

    def test_show_hand_one_card(self):
        """Test show_hand output with one card"""
        import sys
        from io import StringIO
        self.player.hand = "A♣"

        saved_stdout = sys.stdout
        try:
            fake_out = StringIO()
            sys.stdout = fake_out
            self.player.show_hand()
            output = fake_out.getvalue().strip()
            self.assertEqual(output, '1 card: A♣')
        finally:
            sys.stdout = saved_stdout

    def test_show_hand_more_than_two_card(self):
        """Test show_hand output with more than two cards"""
        import sys
        from io import StringIO
        self.player.hand = ["A♣", "2♣", "3♣"]

        saved_stdout = sys.stdout
        try:
            fake_out = StringIO()
            sys.stdout = fake_out
            self.player.show_hand()
            output = fake_out.getvalue().strip()
            self.assertEqual(output, '3 cards: A♣, 2♣, 3♣')
        finally:
            sys.stdout = saved_stdout

    def test_hit_card(self):
        deck = ["A♣", "2♣", "3♣"]
        self.player.hit(deck)
        self.assertEqual(self.player.hand, ["A♣"])
        self.assertEqual(len(deck), 2)


class TestBlackjack(unittest.TestCase):
    def setUp(self):
        self.blackjack = BlackJack()
        self.deck = self.blackjack.deck
        self.suits = ["♣", "♦", "♥", "♠"]
        self.numbers = ["A", "2", "3", "4", "5", "6",
                        "7", "8", "9", "10", "Q", "J",
                        "K"]

    def test_create_deck_attribute(self):
        """Function create_deck needs be 52 cards"""
        deck_size = len(self.deck)
        self.assertEqual(deck_size, 52)

    # def test_hit_card_size_deck_after(self):
    #     """
    #     Hit one card and remove this card from deck
    #     resulting deck needs be have 51 cards
    #     """
    #     self.blackjack.hit()
    #     deck_size = len(self.deck)
    #     self.assertEqual(deck_size, 51)

    # def test_hit_card_valid(self):
    #     """Hit one card and verify if is a valid card"""
    #     card = self.blackjack.hit()
    #     number, suit = card[:-1], card[-1]
    #     self.assertIn(number, self.numbers)
    #     self.assertIn(suit, self.suits)

    # def test_show_points_with_three_cards(self):
    #     """Test show_points calculate with three card"""
    #     import sys
    #     from io import StringIO
    #     self.blackjack.hand = ["A♣", "2♣", "3♣"]

    #     saved_stdout = sys.stdout
    #     try:
    #         fake_out = StringIO()
    #         sys.stdout = fake_out
    #         self.blackjack.show_points()
    #         output = fake_out.getvalue().strip()
    #         self.assertEqual(output, 'Points: 6')
    #     finally:
    #         sys.stdout = saved_stdout

    # def test_show_points_with_two_cards(self):
    #     """Test show_points calculate with two cards"""
    #     import sys
    #     from io import StringIO
    #     self.blackjack.hand = ["10♣", "2♣"]

    #     saved_stdout = sys.stdout
    #     try:
    #         fake_out = StringIO()
    #         sys.stdout = fake_out
    #         self.blackjack.show_points()
    #         output = fake_out.getvalue().strip()
    #         self.assertEqual(output, 'Points: 12')
    #     finally:
    #         sys.stdout = saved_stdout

    # def test_surrender_finish_with_systemexit(self):
    #     """Test if surrender raise SystemExit"""
    #     with self.assertRaises(SystemExit):
    #         self.blackjack.surrender()

    def test_shuffle_deck(self):
        """Deck needs be random sequence after shuffle"""
        from random import shuffle
        deck_before_shuffle = self.deck[0:51]
        shuffle(self.deck)
        deck_after_shuffle = self.deck[0:51]
        self.assertNotEqual(deck_after_shuffle, deck_before_shuffle)

    # Tests missing: show_money and bet

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
