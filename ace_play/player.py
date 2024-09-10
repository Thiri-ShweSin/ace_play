from card import Card

class Player:

    def __init__(self,name):
        self.name = name
        self.hand = []
        self.value = 0
        self.max_card = None

    def draw(self, deck):
        self.hand.append(deck.drawCard())

    def showHand(self):
        for card in self.hand:
            card.show()

    def findMaxCard(self):
        for card in self.hand:
            if card.value >= 10:
                    self.value += 10
            else:
                self.value += card.value
            self.value = int(str(self.value)[-1])
                        
            if self.max_card == None:
                self.max_card = card
            else:
                self.max_card = Card.swapCards(self.max_card, card)