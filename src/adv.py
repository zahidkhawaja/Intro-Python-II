from room import Room
from player import Player
from item import Item

# Items in game
# Items have a name, description, and value
# Value is used to calculate player's net worth
lobster = Item("Lobster", "Delicious crustacean!", 10)
bottle = Item("Bottle", "It's empty!", 5)
flashlight = Item("Flashlight", "A useful source of light.", 5)
pickaxe = Item("Pickaxe", "Useful to mine ore!", 15)
matches = Item("Matches", "Source of fire!", 5)
log = Item("Log", "Just wood!", 5)
gold = Item("Gold", "The jackpot!", 50)
diamond = Item("Diamond", "Solid carbon!", 40)
ruby = Item("Ruby", "Progr- I mean, a beautiful gem!", 30)

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [lobster, bottle]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [pickaxe]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [matches]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [log]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [gold, diamond, ruby]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

playing = True

player_name = input(f"Hello. Please enter your name: ")
current_room = room["outside"]
player = Player(player_name, current_room, [flashlight])
print(f"Nice to meet you, {player.name}!")

playing = True

while(playing):
    print()
    print(f"- You are now at: {player.location.name} - {player.location.description} -")
    print(f"Items in this room: {[x.name for x in player.location.contents]}")
    print()
    decision = input("What do you want to do now? Enter 'h' for help! ")

    try: 
        if decision == "q":
            playing = False
        elif decision == "n":
            player.location = player.location.n_to
        elif decision == "e":
            player.location = player.location.e_to
        elif decision == "s":
            player.location = player.location.s_to
        elif decision == "w":
            player.location = player.location.w_to
        elif decision == "i":
            print()
            print(f"Your inventory: {[x.name for x in player.inventory]}")
        elif decision == "h":
            print()
            print("Options: n (north), e (east), s (south), w (west), i (inventory), p (pickup item), d (drop item), q (quit)")
        elif decision == "p":
            print()
            print(f"Items in this room: {[x.name for x in player.location.contents]}")
            to_pickup = int(input("What would you like to pickup? (Enter the index) "))
            player.pickup_item(player.location.contents[to_pickup])
            print(f"Item picked up: {player.location.contents[to_pickup].name}")
            player.location.contents.remove(player.location.contents[to_pickup])
            print(f"Your inventory now: {[x.name for x in player.inventory]}")
        elif decision == "d":
            print()
            print(f"Your inventory: {[x.name for x in player.inventory]}")
            to_drop = int(input("What would you like to drop? (Enter the index) "))
            player.location.contents.append(player.inventory[to_drop])
            player.drop_item(player.inventory[to_drop])
            last_index = len(player.location.contents) - 1
            print(f"Item dropped: {player.location.contents[last_index].name}")
            print(f"Your inventory now: {[x.name for x in player.inventory]}")

    except AttributeError:
        print()
        print("Oh no! You fell out of the game!")
        print()
        playing = False

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
