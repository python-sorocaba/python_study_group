import os

from core.frenchdeck import FrenchDeck
from core.blackjack import Blackjack
from core.player import Player


def menu():
    """Clear screen and create option menu"""
    msg = ("Jogar: O que gostaria de fazer?\n"
           "\t1. Apostar\n"
           "\t2. Comprar carta\n"
           "\t3. Dobrar aposta\n"
           "\t4. Parar/Finalizar jogada\n"
           "\t5. Chorar pra mãe\n"
           "Digite número desejado: ")
    return msg

if __name__ == "__main__":
    deck = FrenchDeck()
    player = Player("Rafael", 2000.0)
    dealer = Player("Dealer", 0)
    game = Blackjack(dealer, player, deck)
    game.start()
    os.system('cls' if os.name == 'nt' else 'clear')
    print(game.header)
    print(menu())
