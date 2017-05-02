import room, player, items, enemies, time, os, functions
from world import *    

#default game settings etc.
#won needs to be true to win the game
won = False

#create player
player = player.Player()

#set exits and items for every room in world.py
garden1.set_default_exits(diningroom, garden2, None, None)

garden2.set_default_exits(None, None, None, garden1)

kitchen.set_default_exits(storageroom, diningroom, None, None)

diningroom.set_default_exits(hallway1, fireplace, garden1, kitchen)
    
fireplace.set_default_exits(hallway2, None, None, diningroom)

#THe black rose unlocks a hidden room, when player moves into the attic
storageroom.set_default_exits(None, None, kitchen, None)
storageroom.set_item(BlackRose)

hallway1.set_default_exits(staircase, hallway2, diningroom, None)

hallway2.set_default_exits(None, None, fireplace, hallway1)

end.set_default_exits(None, None, None, None)

secret1.set_default_exits(storageroom, None, None, None)

staircase.set_default_exits(None, bedroom, hallway1, None, attic, basement)

bedroom.set_default_exits(None, None, None, staircase)

attic.set_default_exits(None, None, None, None, roof, staircase)
attic.set_item(items.SmallPotion)

roof.set_default_exits(None, None, None, None, None, attic)

basement.set_default_exits(None, None, None, None, staircase, None)


############################################################################################

#Start game
functions.print_home()
functions.press_enter()

functions.print_controlls()
functions.press_enter()

player.move(2)

# Player needs to fine the Black Rose and go to the attic to trigger the first event, which then opens the secret room 1..
while True:
    if player.get_room() is attic and BlackRose in player.get_inventory():
        break
    player.p_input()

functions.clear()
print("Hmm, something is different in here..")
time.sleep(3)
print("You see a writing on the wall.")
time.sleep(3)
print("""As you get closer, you can finally see, that the writing says: "why?" """)
time.sleep(3)
print("Suddendly one of the wooden planks below you breaks and you fall down..")
functions.press_enter()
functions.clear()
player.set_room(staircase)
staircase.change_exits(3, secret1)
attic.change_exits(3, secret1)
print("While slowly opening your eyes, you see something hushing through the door..")
time.sleep(3)
print("The BlackRose disapeard..")
time.sleep(3)
print("The western door of the staircase, which was closed before, is now opened a crack")