from core.frenchdeck import FrenchDeck
from core.player import Player

deck = FrenchDeck()
player = Player("Rafael")
card = deck.pop(0)
player.hand.append(card)
print(player.points)
