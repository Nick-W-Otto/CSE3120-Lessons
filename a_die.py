# a_die.py
"""
Title: Dice roll
Author: Nick Otto
Date: 2021, 02, 16
"""

import random

class Die:

    """
    TO MAKE A DIE OBJECT
    """

    def __init__(self, MAX_VALUE = 6):
        """
        Make a 6-sided die object
        :parameter:
        Max Value: Highest Value for the Die
        """
        self.DIE_MAX = MAX_VALUE
        self.NUMBER = 0


    # --- Setter Methods --- #
    def rollDie(self):
        self.NUMBER = random.randint(1, self.DIE_MAX)


    # --- Getter Methods --- #
    def getRoll(self):
        return self.NUMBER

if __name__ == "__main__":
   D6 = Die(6)
   D8 = Die(8)
   D10 = Die(10)
   D20 = Die(20)

   D6.rollDie()
   print(D6.getRoll())




"""
die1 = Die()
die1.rollDie()
print(die1.getRoll())
die1.rollDie()
print(die1.getRoll())
"""

"""
Dice = []
for i in range(10):
    DICE.append(Die())
    DICE[-1].rollDie()
    print(DICE[-1].getRoll())
"""