from core.player import Player
from core.deck import Deck

if __name__ == "__main__":
    p = Player('Vinicius')
    d = Deck()

    p.hit(d.deck)

    print(p.hand.cards[0].rank)