from decimal import Decimal


class Blackjack:
    # class attributes
    deck = [("K", "hearts"), ("K", "diamonds")]
    money = Decimal('2000.0')
    hand = [("K", "hearts")]

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


if __name__ == "__main__":
    mygame = Blackjack()

    # call instance methods
    mygame.show_cards()
    mygame.show_money()
    mygame.show_hand()
    mygame.show_cls_money()

    # call class method
    Blackjack.show_cls_money()

    # class attributes
    print(Blackjack.deck)
    print(Blackjack.money)

