# -*- coding: utf-8 -*-
import unittest
import blackjack


class TestBlackjack(unittest.TestCase):
    def setUp(self):
        self.deck = blackjack.create_deck()
        self.suits = ["♣", "♦", "♥", "♠"]
        self.numbers = ["A", "2", "3", "4", "5", "6",
                        "7", "8", "9", "10", "Q", "J",
                        "K"]

    def test_create_deck(self):
        """Function create_deck needs be 52 cards"""
        deck_size = len(self.deck)
        self.assertEqual(deck_size, 52)

    def test_shuffle_deck(self):
        """Deck needs be random sequence after shuffle"""
        deck_before_shuffle = self.deck[0:51]
        blackjack.shuffle(self.deck)
        deck_after_shuffle = self.deck[0:51]
        self.assertNotEqual(deck_after_shuffle, deck_before_shuffle)

    def test_hit_card_size_deck_after(self):
        """
        Hit one card and remove this card from deck
        resulting deck needs be have 51 cards
        """
        blackjack.hit(self.deck)
        deck_size = len(self.deck)
        self.assertEqual(deck_size, 51)

    def test_hit_card_valid(self):
        """Hit one card and verify if is a valid card"""
        blackjack.shuffle(self.deck)
        card = blackjack.hit(self.deck)
        number, suit = card[:-1], card[-1]
        self.assertIn(number, self.numbers)
        self.assertIn(suit, self.suits)

    def test_show_hand_one_card(self):
        """Test show_hand output with one card"""
        import sys
        from io import StringIO
        hand = ["A♣"]

        saved_stdout = sys.stdout
        try:
            fake_out = StringIO()
            sys.stdout = fake_out
            blackjack.show_hand(hand)
            output = fake_out.getvalue().strip()
            self.assertEqual(output, '1 card: A♣')
        finally:
            sys.stdout = saved_stdout

    def test_show_hand_more_than_two_card(self):
        """Test show_hand output with more than two cards"""
        import sys
        from io import StringIO
        hand = ["A♣", "2♣", "3♣"]

        saved_stdout = sys.stdout
        try:
            fake_out = StringIO()
            sys.stdout = fake_out
            blackjack.show_hand(hand)
            output = fake_out.getvalue().strip()
            self.assertEqual(output, '3 cards: A♣, 2♣, 3♣')
        finally:
            sys.stdout = saved_stdout

    def test_show_points_with_three_cards(self):
        """Test show_points calculate with three card"""
        import sys
        from io import StringIO
        hand = ["A♣", "2♣", "3♣"]

        saved_stdout = sys.stdout
        try:
            fake_out = StringIO()
            sys.stdout = fake_out
            blackjack.show_points(hand)
            output = fake_out.getvalue().strip()
            self.assertEqual(output, 'Points: 6')
        finally:
            sys.stdout = saved_stdout

    def test_show_points_with_two_cards(self):
        """Test show_points calculate with two cards"""
        import sys
        from io import StringIO
        hand = ["10♣", "2♣"]

        saved_stdout = sys.stdout
        try:
            fake_out = StringIO()
            sys.stdout = fake_out
            blackjack.show_points(hand)
            output = fake_out.getvalue().strip()
            self.assertEqual(output, 'Points: 12')
        finally:
            sys.stdout = saved_stdout

    def test_surrender_finish_with_systemexit(self):
        """Test if surrender raise SystemExit"""
        with self.assertRaises(SystemExit):
            blackjack.surrender()

    # Tests missing: show_money and bet

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
