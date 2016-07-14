from random import shuffle

class Card:
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    def card_value(self):
        if self.rank in list('AJQK'):
            if self.rank == 'A':
                return 1
            else:
                return 10
        else:
            return int(self.rank)

    @property
    def rank(self):
        return self._rank
    
    @property
    def suit(self):
        return self._suit

class Deck:
    numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10"]
    letters = ["A", "Q", "J", "K"]
    suits = ["♣", "♦", "♥", "♠"]

    def __init__(self):
        self._deck = []

        for suit in self.suits:
            for number in self.numbers:
                card = Card(number, suit)
                self._deck.append(card)
            for letter in self.letters:
                card = Card(letter, suit)
                self._deck.append(card)
        shuffle(self._deck)

    @property
    def deck(self):
        return self._deck