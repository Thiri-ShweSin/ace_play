import random
from card import Card

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for suit in Card.suits:
            for value in range(1,14):
                self.cards.append(Card(suit,value))

    def shuffle(self):
        random.shuffle(self.cards)

    def drawCard(self):
        return self.cards.pop()

    def show(self):
        for card in self.cards:
            card.show()