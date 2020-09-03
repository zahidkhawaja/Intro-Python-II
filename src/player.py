# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, location, inventory):
        self.name = name
        self.location = location
        self.inventory = inventory

    def pickup_item(self, item):
        self.inventory.append(item)
    
    def drop_item(self, item):
        self.inventory.remove(item)