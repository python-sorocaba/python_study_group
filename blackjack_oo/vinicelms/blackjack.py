from random import shuffle
from decimal import Decimal

class Deck:
    numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10"]
    letters = ["A", "Q", "J", "K"]
    suits = ["♣", "♦", "♥", "♠"]

    def __init__(self):
        self._cards_value = {}
        self._deck = []

        for suit in self.suits:
            for number in self.numbers:
                self.deck.append("{}{}".format(number, suit))
                self.cards_value[number] = int(number)
            for letter in self.letters:
                self.deck.append("{}{}".format(letter, suit))
                if letter == "A":
                    self.cards_value[letter] = 1
                else:
                    self.cards_value[letter] = 10

    @property
    def deck(self):
        return self._deck

    @property
    def cards_value(self):
        return self._cards_value
    


class Player:
    def __init__(self, money="2000.0"):
        self._money = Decimal(money)
        self._hand = []
        self._points = 0

    @property
    def hand(self):
        return self._hand

    @hand.setter
    def hand(self, value):
        if isinstance(value, str):
            self._hand.append(value)
        elif isinstance(value, list):
            self._hand += value
        else:
            raise ValueError("Value must be string or list!")

    @property
    def points(self):
        return self._points

    @property
    def money(self):
        return self._money

    def get_card_value(self, card):
        cards_value = Deck().cards_value
        return cards_value[card[:-1]]

    def hit_card(self, deck):
        card = deck.pop(0)
        self.hand = card
        self._points += self.get_card_value(card)

    def show_hand(self):
        print("The player have {} cards: {}".format(len(self._hand), ", ".join(self._hand)))

    def show_points(self):
        print("Points in game: {}".format(self.points))

    def show_money(self):
        print("Money in game: {}".format(self.money))

    def deal_cards(self, deck):
        for _ in range(3):
            self.hit_card(deck)

    def bet(self, coin):
        if coin not in (1, 5, 25, 100):
            raise Exception("Invalid coin to bet!")
        if self._money >= coin:
            self._money -= coin
            return coin
        return None

class Blackjack:
    def game_over(self, list_players):
        for player in list_players:
            if player.points >= 21:
                return True
            else:
                return False

if __name__ == "__main__":
    d = Deck()
    game_deck = d.deck
    shuffle(game_deck)

    blackjack = Blackjack()

    p = Player()
    p.deal_cards(game_deck)

    robot = Player()
    robot.deal_cards(game_deck)

    players = [p, robot]

    while(not blackjack.game_over(players)):
        p.hit_card(game_deck)
        robot.hit_card(game_deck)

    for player in players:
        player.show_hand()
        player.show_points()
        player.show_hand

        if player.points == 21:
            print("Winner! 21 points")

        print("*"*20 + "\n")
