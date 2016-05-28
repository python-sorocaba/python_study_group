from random import shuffle
from decimal import Decimal

class Deck:
    numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10"]
    letters = ["A", "Q", "J", "K"]
    suits = ["♣", "♦", "♥", "♠"]

    def __init__(self):
        self._deck = []

        for suit in self.suits:
            for number in self.numbers:
                self.deck.append("{}{}".format(number, suit))
            for letter in self.letters:
                self.deck.append("{}{}".format(letter, suit))

    @property
    def deck(self):
        return self._deck
    

if __name__ == "__main__":
    d = Deck().deck
    print(d)
