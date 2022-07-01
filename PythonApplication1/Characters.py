"""
*Module for AdventureGame.py
Megan Perry
This contains classes, functions and data that relate to the characters in the game.
Characters include Adventurer, Enemies and Friends.  These objects are instantiated here.
Random encounters, battle, and guessing game methods are here.
Extra Credit opportunities: additional characters:
Friends (give gifts), a Pirate Ghost enemy that includes an additional mini-game (guessing game)
"""
from random import *
from Play import *



class Adventurer:
    def __init__(self, name, gems, heartPoints):
        self.name = name
        self.gems = 0
        self.heartPoints = 5

    def addGems(self, x):
        self.gems = self.gems + x
    
    def getGems(self):
        return self.gems

    def addHeartPoints(self, x):
        self.heartPoints = self.heartPoints + x
        if self.heartPoints<=0:
            self.heartPoints = 0
        else:
            self.heartPoints = self.heartPoints
        
    def getHeartPoints(self):
        return self.heartPoints

    def getName(self):
        return self.name

steve = Adventurer("Ocean Steve", 0, 5)

class Enemy:  
    def __init__(self, name, heartPoints):
        self.name=name
        self.heartPoints=heartPoints

    def getEnemyName(self):
        return self.name

    def addHeartPoints(self, x):
        self.heartPoints = self.heartPoints + x
        if self.heartPoints<=0:
            self.heartPoints = 0
        else:
            self.heartPoints = self.heartPoints
            
    def getHeartPoints(self):
        return self.heartPoints
    
enemiesIntrosDict = {} #dictionary holds the intros for the enemies
#4 enemies:
redJellyfish = Enemy("Red Jellyfish", 2)
enemiesIntrosDict[redJellyfish.getEnemyName()] = "You accidentally run into an enemy, Red Jellyfish!\nHopefully you can defeat it without getting stung too many times!"
boxJelly = Enemy("Box Jelly", 3)
enemiesIntrosDict[boxJelly.getEnemyName()] = "An enemy is chasing you! It's Box Jelly.\nDon't be fooled by the small size. Its sting can be deadly!"
shark = Enemy("Great White Shark", 4)
enemiesIntrosDict[shark.getEnemyName()] = "Oh no! The fiercest enemy of the sea, Great White Shark, has you in its sights!\nIt is swimming toward you quickly, wanting a battle!"
ghostPirate = Enemy("Ghost Pirate", 5)
enemiesIntrosDict[ghostPirate.getEnemyName()] = "I am Ghost Pirate and I will win the battle and pillage ye' gems!" 


class RandomEnemyPicker: #This class contains methods for picking the random encounters and the battle with enemy
    def __init__ (self, stepCount):
        self.stepCount = stepCount

    def randomEncounter0to5(self): #This method is for choosing the random encounters type (no encounter, friend, enemy) for steps 1-5, 
                                    #where the friends and enemies make sense for shallow to moderate depth ocean
        chanceEncounter = randrange(0, 3)
        if chanceEncounter == 0: #no encounter
            steve.addGems(100)
            print("You see 100 gems scattered on the sea floor near you.\nYou pick them up.")
            print("        **gems: {}\n        **heart points: {}\n".format(steve.getGems(), steve.getHeartPoints()))
            print("----------------------------------------------------------------")
            input("Press Enter")
        elif chanceEncounter == 1:
            self.battleEnemy()
            print("----------------------------------------------------------------")
            input("Press Enter")
            print("----------------------------------------------------------------")
        else: #friends encounter type-friends give gifts
            friend = randrange(0, 1)
            if friend == 0:
                print("You see your friend Octopus approaching.\nYou see that each of his arms are holding gift bags.")
                print("'Hi {}! I'm so glad to see you! I want to give you one of my giftbags!'".format(steve.getName()))
                print("----------------------------------------------------------------")
                input("Press Enter\n")
                giftbag = randrange(0, 4)
                if giftbag ==0:
                    steve.addHeartPoints(2)
                    print("Octopus gave you 2 heart points! Thank you, Octopus. Keep swimming")
                    print("----------------------------------------------------------------")
                    input("Press Enter")
                    print("----------------------------------------------------------------")
                elif giftbag ==1:
                    steve.addHeartPoints(3)
                    print("Octopus gave you 3 heart points! Thank you, Octopus. Keep swimming")
                    print("----------------------------------------------------------------")
                    input("Press Enter")
                    print("----------------------------------------------------------------")
                elif giftbag ==2:
                    steve.addGems(100)
                    print("Octopus gave you 100 gems! Thank you, Octopus. Keep swimming")
                    print("----------------------------------------------------------------")
                    input("Press Enter")
                    print("----------------------------------------------------------------")
                else:
                    steve.addGems(50)
                    steve.addHeartPoints(1)
                    print("Octopus gave you 1 heart point and 50 gems! Thank you, Octopus. Keep swimming.")
                    print("----------------------------------------------------------------")
                    input("Press Enter")
                    print("----------------------------------------------------------------")
            else:
                print("You see your friend Oyster on the sea floor!\nOyster tells you to swim over annd opens its shell to give you a gift: 100 gems!")
                print("Thank you Oyster! Keep swimming.")
                steve.addGems(100)
            print("        **gems: {}\n        **heart points: {}\n".format(steve.getGems(), steve.getHeartPoints()))
            print("----------------------------------------------------------------")
            input("Press Enter")
            print("----------------------------------------------------------------")


    def randomEncounter6to10(self): #This method is to choose the encounter type for steps 6-10 where the ocean would be deep-no friends, only no encounter or enemy
        chanceEncounter = randrange(0, 2) #no encounter
        if chanceEncounter == 0:
            steve.addGems(100)
            print("You see 100 gems scattered on the sea floor near you.\nYou pick them up.")
            print("        **gems: {}\n        **heart points: {}\n".format(steve.getGems(), steve.getHeartPoints()))
            print("----------------------------------------------------------------")
            input("Press Enter")
            print("----------------------------------------------------------------")
        else:
            self.battleEnemy()
            print("----------------------------------------------------------------")
            input("Press Enter")
            print("----------------------------------------------------------------")


    def chooseEnemyEncounter(self): #This method chooses the enemy for the enemy encounter.  Enemy selection is different depending on steps/ocean depth.
        if self.stepCount <= 6: #shallow-moderate depth enemies
            enemy = randrange(0, 3)
            if enemy == 0:
                battleEnemy = redJellyfish
            elif enemy == 1:
                battleEnemy = boxJelly
            else:
                battleEnemy = shark
        else: #deep water enemies
            enemy = randrange(0, 3)
            if enemy == 0:
                battleEnemy = shark
            else:
                battleEnemy = ghostPirate

        return battleEnemy

    def battleEnemy(self): #This method is the confrontation, also includes a different Ghost Pirate option.  When an enemy dies (runs out of heart points) you won't encounter them again.
        enemy = self.chooseEnemyEncounter()
        if enemy.getHeartPoints() == 0: #if the enemy chosen is dead, then there is no encounter
            steve.addGems(100)
            print("You see 100 gems scattered on the sea floor near you.\nYou pick them up.")
            print("        **gems: {}\n        **heart points: {}\n".format(steve.getGems(), steve.getHeartPoints()))
       
        else: #Ghost Pirate will play guessing game before battle
            if enemy == ghostPirate and ghostPirate.getHeartPoints() != 0:
                PirateGuessGame(steve).playGuessingGame()
            else:
                pass
            enemyIntro = enemiesIntrosDict[enemy.getEnemyName()]
            print(enemyIntro)
            print("**Enemy: {}          ** Enemy's heart points: {}".format(enemy.getEnemyName(), enemy.getHeartPoints()))
            print("----------------------------------------------------------------")
            input("Press Enter")
            print("----------------------------------------------------------------")

            while steve.getHeartPoints() != 0 and enemy.getHeartPoints() != 0:
                #steve attacks enemy
                x = (randrange(1, enemy.getHeartPoints()+1)) #attacks deduct a random amount of heart points from enemy
                enemy.addHeartPoints(-x)
                print("You are attacking! {} loses {} heart points.\n{} has {} heart points left".format(enemy.getEnemyName(), x, enemy.getEnemyName(), enemy.getHeartPoints()))
                print("----------------------------------------------------------------")
                input("Press Enter")
                print("----------------------------------------------------------------")
                if enemy.getHeartPoints() >= 1:
                #enemy attacks steve
                    x = (randrange(1, enemy.getHeartPoints()+1))
                    steve.addHeartPoints(-x)
                    print("{} is attacking you! You lose {} heart points.\nYou have {} heart points left".format(enemy.getEnemyName(), x, steve.getHeartPoints()))
                    print("----------------------------------------------------------------")
                    input("Press Enter")
                    print("----------------------------------------------------------------")
                
            if steve.getHeartPoints() >=1:
                print("***You won the battle!***\n*You will no longer be bothered by {}.*".format(enemy.getEnemyName()))
                
            else:
                print("You lost all of your heart points.\nYou lose!\n********Game Over********")
                input("Press enter to exit")
                quit()

                

class PirateGuessGame: #This class holds the Ghost Pirate guessing game.  You can get gems or a heart point for "winning".
    def __init__(self, steve):
        self.steve = steve
    def playGuessingGame(self):
        print("'Ahoy! I am a Ghost Pirate and I will crush you, Scallywag!\nBut only after we play a guessing game.\n\
        You must guess my secret number first! You have 3 guesses.\n\
        After, you must let me have three chances to guess your secret number!'\n")
        n = randrange(1, 11)
        while True:
            try:
                guess = int(input("It's your guess. Enter a whole number from 1 to 10: "))
            except:
                print("Please enter a number!")
            else:
                break

        count = 1
        while n != guess and count < 3:
            if guess < n:
                print("'Arrgh! Scallywag, Guess higher!'")
                while True:
                    try:
                        guess = int(input("Enter another whole number from 1 to 10: "))
                    except:
                        print("Please enter a number!")
                    else:
                        break
                count = count + 1
            elif guess > n:
                print("'Arrgh! Scallywag, Guess lower!'")
                while True:
                    try:
                        guess = int(input("Enter another whole number from 1 to 10: "))
                    except:
                        print("Please enter a number!")
                    else:
                        break
                count = count + 1
             
        
        if n == guess:
            print("\n'Shiver me timbers! You guessed it! You deserve some of me loot!\nTake 100 of me gems!'\n")
            input("Press Enter\n")
            steve.addGems(100)
            print("        **gems: {}\n        **heart points: {}\n".format(steve.getGems(), steve.getHeartPoints()))
            print("----------------------------------------------------------------")
        else:
            print("\n'You lose, Scallywag!'")
            input("Press Enter\n")
            print("----------------------------------------------------------------")
        print("'Now I get to guess your Scallywag secret number!'")
        while True:
                    try:
                        secretnumber = int(input("Enter your secret whole number 1-10: "))
                    except:
                        print("Please enter a number!")
                    else:
                        break
        pirateGuess = int(randrange(1, 11))
        print("'Ahoy, I guess", pirateGuess, "'")
        input("Press Enter\n")

        guesscount = 1
        while secretnumber != pirateGuess and guesscount < 3:
            if pirateGuess < secretnumber:
                print("\n'Arrrgh!! You hornswaggle cheater! I will guess again!'")
                input("Press Enter\n")
                pirateGuess = randrange(pirateGuess, 11)
                print("'Ahoy, I guess", pirateGuess, "'")
                guesscount = guesscount + 1
            elif pirateGuess > secretnumber:
                print("\n'Arrrgh!! You hornswaggle cheater! I will guess again!'")
                input("Press Enter\n")
                pirateGuess = randrange(1, pirateGuess)
                print("'Ahoy, I guess'", pirateGuess)
                guesscount = guesscount + 1
            else:
                print("'Aye! I guessed your secret number!\nArrgh! Now I will beat you in battle!'")
        if pirateGuess == secretnumber:
            print("\n'I guessed your Scallywag number!'")
            input("Press Enter\n")
        else:
            print("\n'Arrgh!, I couldn't guess your number! I will give you a heart point!\nYou will need it when you battle me, you scurvy dog!'")
            steve.addHeartPoints(1)
            print("        **gems: {}\n        **heart points: {}\n".format(steve.getGems(), steve.getHeartPoints()))
        print("'Now, we battle!'")





        



            





