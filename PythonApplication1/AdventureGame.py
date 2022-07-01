"""
***Run this program to play game***

Megan Perry
This contains main method for executing the game from start to finish.  The details and concerns are separated
and encapsulated in the Play.py files and Characters.py files that must be located in same folder and
imported in order to run the game.
"""
from Play import *
from Characters import *

def main():
    introduction()
    PlayGame(stepDescriptionsList).goThroughSteps()
    youWin()

main()


"""
Extra difficulty added: Enemy availability changes to be appropriate with shallow or deep water
                        Friends that give gifts are available in water that isn't too deep
                        Pirate Ghost has an extra guessing game before battle
Extra Credit opportunities:
additional characters: Friends (give gifts), a Pirate Ghost enemy that includes an additional mini-game (guessing game)
"""
