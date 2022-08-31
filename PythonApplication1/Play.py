"""
*module for AdventureGame.py
Megan Perry
This contains PlayGame and Exit classes, introduction and exit methods, and also other data that is needed to play the game.
Characters.py must be imported for these methods to work.
"""
from Characters import *

stepDescriptionsList = [] #holds the descriptions for each step that the user reads. If I wanted to expand the game, I would store the text in a text file instead.

swimLength1 = "You are just offshore, swimming your first swim-length in the shallows.\n\
The water is clear and you see soft sand, beautiful shells, and little, scurrying crabs.\n\
You feel confident and keep swimming deeper.\n"
swimLength2 = "You are past the shallows, heading toward a swift undercurrent.\n\
You are lucky-the current is going in the direction that you need to swim!\n\
Ride the current to get to your next swim-length faster.\n"
swimLength3 = "You are swimming through a lively coral reef. You see playful fish\n\
and other sea life foraging for food. Don't get distracted. Keep swimming towards your target,\n\
the next swim-length, and ultimately, the shipwreck treasure.\n"
swimLength4 = "You find yourself among a majestic seaweed forest.\n\
The kelp is tall and plentiful. Navigate carefully through the seaweed to your next swim-length."
swimLength5 = "You are among a school of tuna. It is an amazing sight, to be swimming with\n\
hundreds, or perhaps thousands of large, silvery fish. They are all intensely focused on their own role in the\n\
school. They don't notice you. Keep swimming in the direction of the ancient shipwreck.\n"
swimLength6 = "You are at the edge of a rocky plateau. It is very steep and goes deeper than\n\
you would like. Be brave and dive downward off the edge. As the light gets dimmer, use your diving light that\n\
you brought with you.\n"
swimLength7 = "You are swimming through a dark cave. There isn't much that you can see in front of\n\
you besides the occasional blind fish. It is scary, but you are sure that you are swimming in the right\n\
direction. You feel so much relief when you see the outlet of the cave ahead. Stay on alert!\n\
At these depths, big enemies lurk. Swim out and stay focused. You don't have many swim lengths left to go!\n"
swimLength8 = "You are in waters that are slightly murky now, and the depth is just\n\
above where light can reach. It is dim, and you still need your light to see clearly.\n\
You are starting to see scattered debris that looks like it could be from the ancient shipwreck!\n\
You must be getting close! Stay on alert! At these depths, big enemies lurk.\n"
swimLength9 = "You become very excited as you see the shipwreck! Much of it looks\n\
disintegrated by the sea, and the hull is covered with barnacles. Cautiously approach. You are almost there!\n"
swimLength10 = "You are inside the shipwreck! The interior is eerie and\n\
taken over by sea life. It is difficult to maneuver through the wreckage but you are not giving up!\n\
You see the captain's cabin ahead. The door is blocked by the collapsed ceiling and a beam, but you\n\
see a hole where part of the wall is disintegrated. This is just the opportunity you need!\n\
Swim through to claim your treasure!\n"
stepDescriptionsList.append(swimLength1)
stepDescriptionsList.append(swimLength2)
stepDescriptionsList.append(swimLength3)
stepDescriptionsList.append(swimLength4)
stepDescriptionsList.append(swimLength5)
stepDescriptionsList.append(swimLength6)
stepDescriptionsList.append(swimLength7)
stepDescriptionsList.append(swimLength8)
stepDescriptionsList.append(swimLength9)
stepDescriptionsList.append(swimLength10)



class PlayGame:
    def __init__(self, stepDescriptionsList):
        self.stepDescriptionsList=stepDescriptionsList
    def goThroughSteps(self): #executes the body of the game, loops through all of the steps
        stepCount = 0
        for step in self.stepDescriptionsList:
            print(step)
            stepCount += 1
            remainingSteps = len(self.stepDescriptionsList) - stepCount
            print("You can do it! Only {} swim lengths left!\n".format(remainingSteps))
            print("        **gems: {}\n        **heart points: {}\n".format(steve.getGems(), steve.getHeartPoints()))
            #return stepCount
            move = input("Press enter to swim forward or 'q' to quit\n")
            print("----------------------------------------------------------------")
            if move == 'q':
                Exit().quitMethod()
            else:
                if stepCount <=5:
                    RandomEnemyPicker(stepCount).randomEncounter0to5()
                else:
                    RandomEnemyPicker(stepCount).randomEncounter6to10()
            print("----------------------------------------------------------------")

def introduction():
    print("Welcome to 'Ocean Treasure Hunter: Pirate Loot' adventure game!\n\
    You are {}, treasure hunter and diver extraordinaire.\n\
    You are after the pirate loot that is rumored to be on an\n\
    ancient shipwreck, located 10 swim-lengths away from the\n\
    shore where you are right now! The treasure is a cache of\n\
    gems that were looted from ancient royalty by the pirates that\n\
    ruled these seas long ago. Sometimes, the locals will find some\n\
    of these gems randomly littered on the seafloor.\n".format(steve.getName()))
    print("This dive terrain shouldn't be too challenging for an experienced\n\
    diver like you. It would be wise, however, to take the warnings\n\
    from the locals seriously. You may encounter friends during your\n\
    dive, but beware, there are ferocious enemies lurking in the depths!\n")
    print("Swim through 10 swim lengths to reach the captain's cabin of the\n\
    ancient priate shipwreck, which houses a treasure chest with a\n\
    massive loot of precious gems. Collect as many gems as you can\n\
    and protect your heart points, which are your lifeline. Once you\n\
    run out of heart points, your treasure hunt is over!\n")
    print("----------------------------------------------------------------")
    input("Press Enter to Play\n")

def youWin():
    print("!!!!!!YOU WIN!!!!!!\nYou have made it to the captain's cabin!\n\
    You see a barnacle-covered treasure chest sitting in the middle of the room, overflowing with gems.\n\
    They are all yours! You see Your friend Octopus swim through the hole in the wall, and he has graciously\n\
    offered to help you carry your treasure back to shore.\n")
    print("***You get 1000 bonus gems for staying alive and reaching the treasure!***\n")
    steve.addGems(1000)
    print("        **gems: {}\n        **heart points: {}\n".format(steve.getGems(), steve.getHeartPoints()))
    print("----------------------------------------------------------------")
    input("Press Enter to exit")
    print("----------------------------------------------------------------")
    Exit().quitMethod()


class Exit: #exits the game properly
    def __init__(self):
        self.name = ""

    def quitMethod(self):
        print('Thank you for playing "Ocean Treasure Hunter: Pirate Loot" adventure game.')
        print("Please play again!")
        quit()

