import unittest
from decimal import Decimal
from blackjack import Deck, Player, Blackjack

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

    def tearDown(self):
        pass

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player()

    def test_player_hand_property(self):
        self.player.hand = "8♥"
        self.assertEqual(self.player.hand, ["8♥"])
        self.assertRaises(ValueError, setattr, self.player, "hand", 1)

    def test_player_money_property(self):
        self.assertEqual(self.player.money, Decimal("2000.0"))

    def test_hit_card(self):
        deck = ["8♥", "6♣", "2♦"]
        self.player.hit_card(deck)
        self.assertEqual(self.player.hand, ["8♥"])
        self.assertEqual(self.player.points, 8)
        self.assertEqual(len(deck), 2)

    def test_show_points(self):
        deck = ["8♥", "6♣", "2♦"]
        for card in range(3):
            self.player.hit_card(deck)

        import sys
        from io import StringIO
        saved_stdout = sys.stdout
        try:
            fake_out = StringIO()
            sys.stdout = fake_out
            self.player.show_points()
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "Points in game: 16")
        finally:
            sys.stdout = saved_stdout

    def test_show_hand(self):
        self.player.hand = ["8♥", "6♣", "2♦"]
        import sys
        from io import StringIO
        saved_stdout = sys.stdout
        try:
            fake_out = StringIO()
            sys.stdout = fake_out
            self.player.show_hand()
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "The player have 3 cards: 8♥, 6♣, 2♦")
        finally:
            sys.stdout = saved_stdout

    def test_show_money(self):
        import sys
        from io import StringIO
        saved_stdout = sys.stdout
        try:
            fake_out = StringIO()
            sys.stdout = fake_out
            self.player.show_money()
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "Money in game: 2000.0")
        finally:
            sys.stdout = saved_stdout

    def test_deal_cards(self):
        deck = ["8♥", "6♣", "2♦", "10♦", "3♣"]
        self.player.deal_cards(deck)
        self.assertEqual(self.player.hand, ["8♥", "6♣", "2♦"])
        self.assertEqual(deck, ["10♦", "3♣"])
        self.assertEqual(len(deck), 2)

    def test_bet(self):
        self.assertEqual(self.player.bet(100), 100)
        self.assertRaises(Exception, lambda: self.player.bet(10))

    def test_get_card_value(self):
        self.assertEqual(self.player.get_card_value("6♣"), 6)


    def tearDown(self):
        pass

class TestBlackjack(unittest.TestCase):
    def setUp(self):
        self.blackjack = Blackjack()
        self.player = Player()

    def test_game_over_end_game(self):
        deck = ["8♥", "6♣", "2♦", "10♦"]
        for card in range(len(deck)):
            self.player.hit_card(deck)
        self.assertTrue(self.blackjack.game_over([self.player])) """Method return True to Game Over"""

    def test_game_over_continue_game(self):
        deck = ["8♥", "6♣", "2♦"]
        for card in range(len(deck)):
            self.player.hit_card(deck)
        self.assertFalse(self.blackjack.game_over([self.player])) """Method return False to Game Over, i.e., the game continues"""

    def tearDown(self):
        pass
