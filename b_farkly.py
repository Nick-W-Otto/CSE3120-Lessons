"""
Title: Farkle
Author: Nick Otto
Date Created: 2021, 02, 17
"""

from a_die import Die

"""
Players have six dice. They take turns rolling the dice, holding at least one die per roll. Each round a player rolls up to three times. Various combination are worth points
"""

class Player:
    """
    Represents each player in the game, the player must be able to
    - roll 6 dice
    - hold specific dice per roll
    - update a score
    - name of the player
    """

    def __init__(self, NAME):
        self.NAME = NAME
        self.SCORE = 0
        self.DICE = [Die(), Die(), Die(), Die(), Die(), Die()]
        self.HELD = []
        self.ROLL_NUM = 0

    # --- Modifier Methods --- #

    ## Inputs

    def setScore(self):
        """
        Player will manually enter a score.
        :return: Players Score
        """
        self.displDice()
        ## Inputs
        SCORE_ROUND = int(input("Score: "))
        ## Processing
        self.SCORE = self.SCORE + SCORE_ROUND
        ## Outputs
        print(f"{self.NAME}'s Score: {self.SCORE}")
    ## Processing

    def rollDice(self):
        """
        Player will roll all unheld Dice
        :return: Amount of roll die and values
        """
        for die in self.DICE:
            die.rollDie()
        self.ROLL_NUM = self.ROLL_NUM + 1

    def holdDie(self):
        """
        Players selects an unheld die and holds it
        :return:
        """
        ## Display Die Values
        print("Select a die to hold")
        for i in range(len(self.DICE)):
            print(f"{i + 1}. {self.DICE[i].getRoll()}")

        ## Input which die to hold
        DIE = int(input("> "))

        ## Processing -- Move die from self.DICE to self.HOLD
        self.HELD.append(self.DICE.pop(DIE - 1))

        ## Outputs

        self.displDice()

        ## Ask to hold more Dice
        if len(self.DICE) > 0:
            AGAIN = input("Hold more dice? (y/N ")
            AGAIN = AGAIN.upper()
            if AGAIN == "Y":
                return self.holdDie()

        # Ask to reroll dice
        if self.ROLL_NUM < 3:
            END = input("Roll again (Y/n)")
            END = END.upper()
            if END == "N":
                self.ROLL_NUM = 3

    def endTurn(self):
        self.DICE = self.DICE + self.HELD
        self.HELD = []
        self.ROLL_NUM = 0

    # --- Accessor Methods --- #

    ## Outputs

    def displDice(self):
        print("Dice Remaining: ", end=" ")
        for die in self.DICE:
            print(die.getRoll(), end=" ")
        print("")  # Create a new line
        print("Dice Held: ", end=" ")
        for die in self.HELD:
            print(die.getRoll(), end=" ")
        print("")

    def getROLL_NUM(self):
        return self.ROLL_NUM

    def getScore(self):
        return self.SCORE

    def getNAME(self):
        return self.NAME

class Game:
    """
    Manages the player turns and determines a winner
    """

    def __init__(self):
        self.PLAYERS = []
        self.WINNER = False


    def setup(self):
        """
        Tasks to start the game
        """
        print("Welcome to Farkle")
        NUM_PLAYERS = int(input("How many Gamers? "))
        for i in range(NUM_PLAYERS):
            NAME = input("Name: ")
            self.PLAYERS.append(Player(NAME))


    def run(self):
        """
        Main Program code --> running of program
        """
        # Change Turns and test for a winner at the end of the round
        while not self.WINNER:
            for player in self.PLAYERS:
                print(f"{player.getNAME()}'s Turn")
                while player.getROLL_NUM() < 3:
                    player.rollDice()
                    player.holdDie()
                player.endTurn()
                player.setScore()
            for player in self.PLAYERS:
                if player.getScore() >= 1000:
                    self.WINNER = True
                    break

if __name__ == "__main__":
    GAME = Game()
    GAME.setup()
    GAME.run()
