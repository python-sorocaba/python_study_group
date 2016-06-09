import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    """This class is based on ...
    Sample code for Chapter 1 - "The Python Data Model"
    From the book "Fluent Python" by Luciano Ramalho (O'Reilly, 2015)
    http://shop.oreilly.com/product/0636920032519.do
    """
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __setitem__(self, position, value):
        self._cards[position] = value

    def pop(self, index):
        return self._cards.pop(index)
