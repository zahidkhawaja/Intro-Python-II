from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", ["Lobster", "Bottle"]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ["Lighter"]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ["Log", "Binoculars"]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ["Pickaxe"]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", ["Gold", "Ruby", "Diamond"]),
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
player = Player(player_name, current_room, ["Flashlight"])
print(f"Nice to meet you, {player.name}!")

playing = True

while(playing):
    print()
    print(f"You are now at: {player.location.name} - {player.location.description}")
    print(f"Items in this room: {player.location.contents}")
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
            print(f"Your inventory: {player.inventory}")
        elif decision == "h":
            print()
            print("Options: n (north), e (east), s (south), w (west), i (inventory), q (quit)")
        elif decision == "p":
            print()
            to_pickup = int(input("What would you like to pickup? (Enter the index) "))
            player.pickup_item(player.location.contents[to_pickup])
            print(f"Item picked up: {player.location.contents[to_pickup]}")
            player.location.contents.remove(player.location.contents[to_pickup])
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
