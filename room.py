import random, enemies

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description 
        self.exits = [None, None, None, None]
        self.enemy = None
        self.item = None

    def get_name(self):
        return self.name
    
    def set_description(self, description):
        self.description = description
    
    def get_description(self):
        return self.description
        
    def set_default_exits(self, north, east, south, west):
        self.exits = [north, east, south, west]

    def reset_exits(self):
        self.exits = self.oldexits

    #direction needs to be a number from 0 to 3 for casual rooms and 0 to 5 for staircases
    def change_exits(self, direction, room):
        self.oldexits = self.exits
        self.exits[direction] = room

    def get_exit(self):
        return self.exits

    def get_exit_name(self):
        exitname = []
        for i in range (0, 4):
            if self.get_exit()[i] is None:
                exitname.extend(["None"])
            else:
                exitname.append(self.get_exit()[i].get_name())
        return exitname
    
    def set_item(self, item):
        self.item = item

    def get_item(self):
            return self.item


    def get_enemy(self):
        if self.enemy == None:
            return None
        else:
            return self.enemy

    def spawn_enemy(self, level):
        if self.enemy == None and random.randint(0, 2) == 1:
            if 0 < level < 3:
                self.enemy = enemies.Spider()
            elif 2 < level < 6:
                self.enemy = enemies.BigSpider()
            elif 5 < level < 9:
                self.enemy = enemies.HugeSpider()
            elif 8 < level < 12:
                self.enemy = enemies.Ghost()

    def despawn_enemy(self):
        self.enemy = None




class Staircase(Room):
    def __init__(self, name, description):
        super().__init__(name, description)

    def set_default_exits(self, north, east, south, west, up, down):
        self.exits = [north, east, south, west, up, down]

    def get_exit_name(self):
        exitname = []
        for i in range (0, 6):
            if self.get_exit()[i] is None:
                exitname.extend(["None"])
            else:
                exitname.append(self.get_exit()[i].get_name())
        return exitname
