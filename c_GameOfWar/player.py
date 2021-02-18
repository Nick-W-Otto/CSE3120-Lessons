"""
Title: Playing cards Player
Author: Nick Otto
Date: 2021. 02, 18
"""

from card import Card
from deckpy import Deck

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
