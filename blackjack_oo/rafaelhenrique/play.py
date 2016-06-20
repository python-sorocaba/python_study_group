from core.frenchdeck import FrenchDeck
from core.blackjack import Blackjack
from core.player import Player

deck = FrenchDeck()
player = Player("Rafael", 2000.0)
dealer = Player("Dealer", 0)
game = Blackjack(dealer, player, deck)
game.start()
print(len(dealer.hand) == 2)
