"""
Title: Playing cards Deck
Author: Nick Otto
Date: 2021. 02, 18
"""

from card import Card
from random import randrange

class Deck:
    """
    Creates a deck of cards
    """

    def __init__(self):
        self.DECK = []
        for i in range(1, 5):
            for j in range(1, 14):
                self.DECK.append(Card(i, j))



    # Modifier Methods #
    def drawRandomCard(self):
        return self.DECK.pop(randrange(len(self.DECK)))



    # Accessor Methods #
    def getDeck(self):
        return self.DECK

if __name__ == "__main__":
    DECK = Deck()
    CARD = DECK.drawRandomCard()
    print(CARD)
    print(DECK.getDeck())



