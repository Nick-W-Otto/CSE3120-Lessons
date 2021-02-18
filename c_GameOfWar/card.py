"""
Title: Playing cards
Author: Nick Otto
Date: 2021. 02, 18
"""

class Card:

    """
    Create Playing Card Object
    """

    SUITS = {
        1: "Diamonds",
        2: "Clubs",
        3: "Hearts",
        4: "Spades"
    }

    VALUES = {
        1: "Ace",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "10",
        11: "Jack",
        12: "Queen",
        13: "King"
    }

    def __init__(self, SUIT, VALUE):
        self.SUIT = SUIT
        self.VALUE = VALUE

    def __str__(self):
        return f"{Card.VALUES[self.VALUE]} of {Card.SUITS[self.SUIT]}"

    def __repr__(self):
        return f"<Card Object at {Card.VALUES[self.VALUE]} or {Card.SUITS[self.SUIT]}>"

    # Modifier Methods #

    # Accessor Methods #

    def getValue(self):
        return self.VALUE

