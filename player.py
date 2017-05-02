import items, random, functions
from world import *

class Player():
    #initiate player at level 1
    def __init__(self):
        self.inventory = [] #List of items in inventory
        self.lastRoom = None
        self.currentRoom = diningroom
        self.hp = 20 #hp == health points
        self.level = 1
        self.exp = 0 #exp == experience points
        self.weapon = items.Fist()
        self.ap = 1 + self.get_weapon().get_ap() #ap == Attack points
        self.command = ["exit", "w", "a", "s", "d", "north", "south", "west", "east", "up", "down", "fight", "shop","info","search", "exit", "controlls"]
    
    #get player room
    def get_room(self):
        return self.currentRoom

    def set_room(self, room):
        self.currentRoom = room

    def get_last_room(self):
        return self.lastRoom

    def set_last_room(self, room):
        self.lastRoom = room
    
    #get player inventory//returns list
    def get_inventory(self):
        return self.inventory
    
    #remove item from inventory list
    def remove_from_inventory(self, itemIndex):
        self.inventory.remove(itemIndex)

    #get player ap
    def get_ap(self):
        return self.ap

    #get player hp
    def get_hp(self):
        return self.hp
    
    #get player weapon
    def get_weapon(self):
        return self.weapon
    
    #get player level
    def get_level(self):
        return self.level
    
    #get player experience
    def get_exp(self):
        return self.exp
    
    #gain experience (for example after an achievment or killing an enemy)
    def gain_exp(self):
        if self.get_level() <3:
            self.exp += random.randint(1,2)
        elif self.get_levle() <6:
            self.exp += random.randint(2,4)
        else:
            self.exp += random.randint(4,6)
        if self.exp >= 3 * self.get_level():
            self.level += 1
            self.exp = 0
            self.ap += random.randint(0,2)
    
    #create user interface. Always refreshes the console for a more clear game experience
    def UI(self):
        functions.clear()
        #print current player stats in the first row and the room name + exits after
        print("Level: " + str(self.get_level()) + "(" + str(self.get_exp()*10) + "%)" + " Weapon: " + str(self.get_weapon().get_name())  + "  AP: " + str(self.get_ap()) +  "  HP: " + ("*" * self.get_hp()) 
        + "\n______________________________________________________________________" 
        + "\nCurrent room: " + self.get_room().get_name() + "   Last room: " + self.get_last_room().get_name()
        + "\n"
        + "\nNorth:  " + str(self.get_room().get_exit_name()[0]) 
        + "\nEast:   " + str(self.get_room().get_exit_name()[1])
        + "\nSouth:  " + str(self.get_room().get_exit_name()[2]) 
        + "\nWest:   " + str(self.get_room().get_exit_name()[3])) 
        #check if room is a staircase == lenght of exit list > 4 
        if len(self.get_room().get_exit()) > 4:
            print("up:     " + str(self.get_room().get_exit_name()[4])
            + "\nDown:   " + str(self.get_room().get_exit_name()[5]))
        if self.get_room().get_enemy() is not None:
            print("\nEnemy: " + str(self.get_room().get_enemy().get_name()))
        else:
            print("\nEnemy: None")
        print("_____________________________________________________________________")
        print(str(self.get_room().get_description()))

    #use this everytime you enter another room. Move() checks for enemies in the room and spawns a new enemy if there is no enemy. also Refreshes the Console to print a new UI, with the new room infos.
    def move(self, direction):
        self.set_last_room(self.get_room())
        self.set_room(self.get_room().get_exit()[direction])
        if self.get_room().get_enemy() is None:
            self.get_room().spawn_enemy(self.level)
        self.UI()
        
    #fight() calculates the player and enemy hp after the fight. To calculate the dmg to everyone involved into the fight with the given attack points. Also checks if player or enemy is dead after the fight.
    def fight(self):
        self.get_room().get_enemy().loose_hp(self.get_ap() + random.randint(-(int(self.get_ap()/2)), int(self.get_ap()/2)))
        self.hp -= (self.get_room().get_enemy().get_ap()+random.randint(-(self.get_room().get_enemy().get_ap()), self.get_room().get_enemy().get_ap()))
        if self.hp <= 0:
            clear()
            print("""
            You lost the fight...
               GAME OVER
            """)
            exit()
        elif self.get_room().get_enemy().is_alive == True:
            self.UI()
            print("You dealt " + str(self.ap) + "damage.")
        else:
            self.get_room().despawn_enemy()
            self.gain_exp()
            self.UI()
            print("You won the fight!")
        print("Remaining health: " + str(self.hp))
    
    #search the room for items. Prints the item and adds it to the inventory, if something was found. Otherwise prints that there is no item in the room.
    def search_room(self):
        if self.get_room().get_item() is not None:
            self.inventory.append(self.get_room().get_item())
            print ("You found a " + self.get_room().get_item().get_name() + "!")
        else:
            print("There is nothing in this room...")        

    #Checks for potion in inventory and uses it, if there is one.
    def use_potion(self):
        if items.SmallPotion in self.get_inventory():
            potion = items.SmallPotion()
            i = self.get_inventory().index(items.SmallPotion)
        elif items.MediumPotion in self.get_inventory():
            potion = items.MediumPotion()
            i = self.get_inventory().index(items.MediumPotion)
        elif items.BigPotion in self.get_inventory():
            i = self.get_inventory().index(items.BigPotion)
            potion = items.BigPotion()
        self.hp = potion.get_heal()
        self.remove_from_inventory(i)

        print("You regenerated " + str(potion.get_heal()) + " HP")

    #Gets input from player and processes it. 
    def p_input(self):
        
        pinput = input("> ")
        
        #check if command is allowed
        if pinput in self.command:

            #movement inputs:
            if pinput == ("w" or "north") and self.get_room().get_exit()[0] is not None:
                self.move(0)
                    
            elif pinput == ("d" or "east") and self.get_room().get_exit()[1] is not None:
                self.move(1)
                    
            elif pinput == ("s" or "south") and self.get_room().get_exit()[2] is not None:
                self.move(2)
                    
            elif pinput == ("a" or "west") and self.get_room().get_exit()[3] is not None:
                self.move(3)

            elif pinput == "up":
                try:
                    self.get_room().get_exit()[4]
                    if self.get_room().get_exit()[4] is not None:
                        self.move(4)

                except:
                    print("This is not possible...")

            elif pinput == "down":
                try:
                    self.get_room().get_exit()[5]
                    if self.get_room().get_exit()[5] is not None:
                        self.move(5)

                except:
                    print("This is not possible...")
            
            #checks if enemy is in room and calculates dmg to enemy and player
            elif pinput == "fight":
                if self.currentRoom.get_enemy() is not None:
                    self.fight()
                    
                else:
                    print("Do you see any enemies in here?!!?!")
            
            #use potion !!!!!!!!!!!!! DOES NOT WORK AT THE MOMENT, NEEDS TO BE REFACTORED
            elif pinput == "use potion":
                if items.Potion in self.get_inventory():
                    self.hp += self.inventory[Potion].get_heal()

            #print room description
            elif pinput == "info":
                print(str(self.get_room().get_description()))
            
            #search room
            elif pinput == "search":
                self.search_room()
            
            #prints all controlls
            elif pinput == "controlls":
                functions.print_controlls()

            #exit game
            elif pinput == "exit":
                exit()
            
            #if processing failes (e.g. Room cannot be changed or no potion)
            else:
                print("That's not possible for me...")

        else:
            print("This is not a known command...")