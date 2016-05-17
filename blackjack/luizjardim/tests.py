# -*- coding: utf-8 -*-

import blackjack
import unittest


class TestBlackJack(unittest.TestCase):

    def setUp(self):
        self.deck = blackjack.create_deck()

        self.faces = ["A", "2", "3", "4", "5", "6",
             "7", "8", "9", "10", "Q", "J",
             "K"]
        self.suits = ["♣", "♦", "♥", "♠"]
        self.money = blackjack.show_money()


    def test_len_deck(self):
        """This test verify if the deck is French with 52 cards"""
        self.assertEqual(len(self.deck), 52)

    def test_shuffle_deck(self):
        """This test guarantee the deck is shuffled"""
        self.deck_shuffle = blackjack.shuffle_deck(self.deck)
        self.assertNotEqual(self.deck_shuffle, self.deck)

    def test_hit_card_is_valid(self):
        """This test valid the face of the hit card"""
        card_hit = blackjack.hit_card(self.deck)
        face_of_card = card_hit[:-1]
        self.assertIn(face_of_card, self.faces)


    def test_show_money(self):
        self.assertEqual(self.money, blackjack.show_money())

    def test_bet(self):
        self.assertTrue(self.money, blackjack.bet())

    pass


if __name__ == '__main__':

    unittest.main()