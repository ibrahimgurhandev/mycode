#!/usr/bin/python3
import os
from random import randint
import dice


class SwordMaster(object):
    health = 150
    strength = 14
    defence = 13
    magic = 11
    inv = ["sword", "shield"]


class Fighter(object):
    health = 150
    strength = 40
    defence = 5
    magic = 1
    inv = ["sword", "shield"]


class Mage(object):

    health = 150
    strength = 6
    defence = 7
    magic = 22
    inv = ["fireball", "teleport"]

class Paladin(object):
    health = 150
    strength = 15
    defence = 25
    magic = 5
    inv = ["spear", "shield", 'heal']


# MONSTERS
class Werewolf(object):
    health = 50
    strength = 35
    defence = 25
    magic = 1
    name = "Werewolf"


class Dragon(object):
    health = 90
    strength = 35
    defence = 25
    magic = 21
    name = "Dragon"


class Troll(object):
    health = 45
    strength = 20
    defence = 17
    magic = 2
    name = "Troll"


def roll_enemy(Werewolf,Dragon,Troll):
    enemyList = [Werewolf,Dragon,Troll]
    dice = randint(0,2)
    enemy = enemyList[dice]
    return enemy


def fight_monster():
    os.system('clear') # clear the screen

    enemy = roll_enemy(Werewolf,Dragon,Troll)
    print("You have encountered a ", enemy.name)
    print("you have 2 options...")
    while enemy.health > 0:
        os.system('clear')  # clear the screen
        choice = input("1. Attack \n2. RUN!\n>")

        if choice == "1":
            print("You swing your weapon, attacking the", enemy.name)
            hit_dice = randint(0, 10)
            if hit_dice > 3:
                enemy.health = enemy.health - player1.strength
                print("You hit the enemy, their health is now....", enemy.health)

                if enemy.health > 1:
                    player1.health = player1.health - (enemy.strength / player1.defence)
                    print("The", enemy.name, "takes a swing, it hits you leaving", player1.health)
                    gameOver(player1)

                else:
                    if enemy.name == "Dragon":
                        enemy.health = 20

                    elif enemy.name == "Werewolf":
                        enemy.health = 10

                    elif enemy.name == "Troll":
                        enemy.health = 15

                    print("You have defeated the", enemy.name)
                    break
            else:
                print("Your attack missed")
                print("The", enemy.name, "hits you for full damage")
                player1.health = player1.health - enemy.strength
                print("You now only have", player1.health, "remaining")
                gameOver(player1)

        elif choice == "2":
            print("you try to run....")
            dice = randint(1, 10)
            if dice > 4:
                print("you got away unscratched!")
                break
            else:
                print("You try to run but slip and fall")
                print("You try to defend but cannot, the enemy hits you for full damage...")
                player1.health = player1.health - enemy.strength
                print("Your health is now", player1.health)
                gameOver(player1)
        else:
            print("number not allowed, please only type 1, or 2")


def showInstructions():
    # print a main menu and the commands
    print('''
WELCOME TO ADVENTURE QUEST!
OBJECTIVE: Complete quests, fight dragons and level up to to become the most powerful fighter. 
--------
Actions:
    GO [north, south, east, west, up, down]
    GET [item, spell]
    USE [item]
    'INFO' for more information
    'INV' to see your inventory'
    Type 'q' to quit!
''')


def gameOver(player):
    if player.health < 1:
        print("You have no health left")
        print("Thanks for playing...")
        exit()


def showStatus(): # display the player's status
    if 'item' in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
#    print('=================')


def select_class():
    print("Select your hero!")
    selection = input("1. Paladin \n2. Mage \n3. SwordMaster \n4. Fighter \n>")
    if selection == "1":
        player = Paladin
        print("You have selected the Paladin...Paladins are warriors who fight for the Light, not only specializing in combat, but also in healing")
        print("These are their stats...")
        print("Health - ", player.health)
        print("Strength - ", player.strength)
        print("Defence - ", player.defence)
        print("Magic - ", player.magic)
        return player

    elif selection == "2":
        player = Mage
        print("You have selected the Mage...Mages have cultivated their latent gift in magic at a basic level--that of Elemental Magic. Upon "
            "initiation, mages may seek further knowledge in other realms of magic, such as summoning, necromancy, "
            "healing magic, and illusionary magic.")
        print("These are their stats...")
        print("Health - ", player.health)
        print("Strength - ", player.strength)
        print("Defence - ", player.defence)
        print("Magic - ", player.magic)
        return player

    elif selection == "3":
        player = SwordMaster
        print("You have selected the SwordMaster...Sword Master is the last descendant of Fuxi, and his Fuxi Sword has mysterious magical powers")
        print("These are their stats...")
        print("Health - ", player.health)
        print("Strength - ", player.strength)
        print("Defence - ", player.defence)
        print("Magic - ", player.magic)
        return player

    elif selection == "4":
        player = Fighter
        print('You have selected the Fighter...Fighters focus mainly on their Strength attribute to master the basic arts of being a warrior.')

        print("These are their stats...")
        print("Health - ", player.health)
        print("Strength - ", player.strength)
        print("Defence - ", player.defence)
        print("Magic - ", player.magic)
        return player

    else:
        print("Only press 1, 2, 3 or 4")
        select_class()


# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
rooms = {

    'Forest': {
        'south': 'Castle',
        'east': 'Temple of Hope',
        'item': 'potion',
        'down': 'Dungeon',
        'west':'Arena',
        'info': 'You are currently in a dark forest, with eery shadows moving around you. Move out of the forest before its too late '
    },
    'Dungeon': {
        'up': 'Forest',
        'monster':'yes',
        'info':'You have arrived in dark dungeon that is filled with monsters. The only way out is to go up'
    },

    'Castle': {
        'info': 'You are in an abandoned castle. The walls are crumbling. It looks like there is nothing special here, but is that really the case',
        'north': 'Forest',
        'item': 'temple key'
    },
    'Temple of Hope': {
        'west': 'Forest',
        'south': 'Arena',
        'item': 'map',
        'info': 'You have found the hidden Temple of Hope and activated a special Quest. Take the map to help you in your quest'
    },
    'Arena': {
        'north': 'Temple of Hope',
        'monster':'yes',
        'west':'Forest',
        'info': 'You are in a battle Arena.'
    }
}
# start the player in the Hall
currentRoom = 'Forest'


# select class

showInstructions()

player1 = select_class()

# loop forever
while True:

    showStatus()

    # get the player's next 'move'
    # .split() breaks it up into an list array
    # eg typing 'go east' would give the list:
    # ['go','east']
    move = ''
    while move == '':
        move = input('>')

    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]
    move = move.lower().split(" ", 1)
    os.system('clear') # clear the screen
    if move[0] == 'look':
        if 'info' in rooms[currentRoom]:
            print(rooms[currentRoom]['info'])
        else:
            print('You can\'t see anything.')

    if move[0] in ['q', 'quit]']:
        print("Are you sure you want to quit? Yes/No")
        quit_query = input('>')
        if quit_query.lower() in ['y', 'yes']:
            print("Thanks for playing!")
            gameOver(player1)

    # if they type 'go' first
    if move[0] == 'go':
        os.system('clear')  # clear the screen
        # check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            # set the current room to the new room
            if rooms[currentRoom][move[1]] == "Temple of Hope" and 'key' not in player1.inv:
                print("You cannot enter the temple without the key")
            else:
                currentRoom = rooms[currentRoom][move[1]]
                if currentRoom == 'Arena':
                    fight_monster()
                elif currentRoom == 'Dungeon':
                    fight_monster()
                print(rooms[currentRoom]['info'])
        # there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    # if they type 'get' first
    if move[0] == 'get':
        os.system('clear')  # clear the screen

        # if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            # add the item to their inventory
            player1.inv += [move[1]]
            # display a helpful message
            print(move[1] + ' got!')
            # delete the item from the room
            del rooms[currentRoom]['item']
        # otherwise, if the item isn't there to get
        else:
            # tell them they can't get it
            print('Can\'t get ' + move[1] + '!')
    if move[0] == 'inv':
        print("You current have: ", player1.inv)
