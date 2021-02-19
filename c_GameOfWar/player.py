"""
Title: Playing cards Player
Author: Nick Otto
Date: 2021. 02, 18
"""

# Two player classes with different arrays and pop values out of the deck into their hand using random pops

from card import Card
from deckpy import Deck
from random import randrange

class Player:
    """
    Creates the Player and gives them cards to hold
    """

    def __init__(self, NAME):

        self.NAME = NAME
        self.HAND = []

    # --- Modifier Methods --- #

    # Inputs #



    # Processing #





    # Outputs #

    # --- Accessor Methods --- #

    def getName(self):
        return self.NAME

    def getDeck(self):
        return self.HAND

if __name__ == "__main__":
    DECK = Deck()
    p1Deck = []
    p2Deck = []

    splitDeck = []

    splitDeck.append(DECK.pop(randrange(1, 26)))
    for i in range(26):
        p1Deck.append(DECK.pop(randrange(1, len(DECK))))
    print(p1Deck)