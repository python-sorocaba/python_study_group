from decimal import Decimal


class Blackjack:
    # class attributes
    deck = [("K", "hearts"), ("K", "diamonds")]
    money = Decimal('2000.0')
    hand = [("K", "hearts")]

    def __init__(self, deck=None, money=Decimal('1000.0')):
        if not deck:
            deck = [("A", "clubs"), ("A", "spades")]

        # instance attributes
        self.deck = deck
        self.money = money

    # instance methods
    def show_cards(self):
        print("show_cards: {}".format(self.deck))

    def show_money(self):
        print(self)
        print("show_money: {}".format(self.money))

    def show_hand(self):
        print(self)
        print("show_hand: {}".format(self.hand))

    # class method
    @classmethod
    def show_cls_money(cls):
        print(cls)
        print("show_cls_money: {}".format(cls.money))

    @staticmethod
    def say_hello(name):
        print("Hello {}!".format(name))

if __name__ == "__main__":
    print("mygame: \n")
    mygame = Blackjack()

    mygame.show_cards()
    mygame.show_money()
    mygame.show_cls_money()
    mygame.show_hand()

    print("\nClass atributtes:")
    print("deck: {}".format(Blackjack.deck))
    print("money: {}".format(Blackjack.money))

    print("\n\nmygame2: \n")
    mygame2 = Blackjack(
        deck=[("10", "clubs"), ("10", "spades")],
        money=Decimal('10.0'))

    mygame2.show_cards()
    mygame2.show_money()

    print("\n\nmygame3: \n")
    mygame3 = Blackjack(
        deck=[("9", "clubs"), ("9", "spades")])

    mygame3.show_cards()
    mygame3.show_money()

    print("staticmethod:")
    mygame3.say_hello("Rafael")
    Blackjack.say_hello("Rafael")

