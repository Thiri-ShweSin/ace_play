from deck import Deck
from card import Card
from player import Player

class Game:
    def __init__(self):
        self.players = []
        self.winner = None
        self.deck = Deck()
        self.deck.shuffle()
        
    def play(self):
        num = int(input("How many players (up to 5) to start a game?"))
        if num<=5:
            for i in range(num):
                name = input("Enter name:")
                player = Player(name)
                self.players.append(player)
        else:
            print("We accept at most 5 players. Please try again.")
            self.play()

    def dealCards(self, player):
        for i in range(2):
            player.draw(self.deck)
        
        print("Your cards are:")
        player.showHand()
        print("*"*30)

        ans = input("One more card(y/n), {}:".format(player.name))
        if(ans.lower()=='y'):
            player.draw(self.deck)
            player.showHand()


    def playerMaxCard(self):
        for player in self.players:
            player.findMaxCard()
            print(player.name, "value=>",player.value,"max_value=>",player.max_card.value,"max_suit",player.max_card.suit)
            # player.showHand()
            # print("*"*30)

    def findWinner(self):
        for player in self.players:
            if self.winner == None:
                self.winner = player
            else:
                if self.winner.value == player.value:
                    if len(player.hand) < len(self.winner.hand):
                        self.winner = player
                    elif len(player.hand) == len(self.winner.hand):
                        self.winner.max_card = Card.swapCards(self.winner.max_card,player.max_card)
                        if self.winner.max_card in player.hand:
                            self.winner = player     
                elif player.value > self.winner.value:
                        self.winner = player
        return str("Winner is: " + self.winner.name)

    def run(self):
        self.play()
        self.dealCards()
        self.playerMaxCard()
        self.findWinner()