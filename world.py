import room, items


#Create all room and items instances that are in the world by default
#floor 0
garden1 = room.Room("Garden (west)",
"""You find yourself in a huge garden.
A bench stands beneath a withered oak tree.
In the north you can see an old mansion covered in black roses.
""")

garden2 = room.Room("Garden (east)",
"""You followed a path to the east side of the garden.
At the path's end you see more withered plants with a black rose standing in the middle.
Next to you is a sign which says: "RUN...!"
""")

kitchen = room.Room("Kitchen",
"""A few pots are standing on the cooker. It seems like someone was recently cooking in here.
Some dishes are lying on ground. Next to them a chair fell over and the wooden planks are covered in Blood.
""")

diningroom = room.Room("Dining Room", 
"""A dark wooden table is standing in the middle of the room.
Around it are wooden chairs with red padding and some golden accents.
Some of the candles on the table are burning. You can see the old oak tree through the windows.""")

fireplace = room.Room("Fireplace Room",
"""There is a red armchair next to the burning fireplace.
Some old pictures are covering the walls. 
As you walk to the room you see a skull in one corner.
A cat is sitting next to the fireplace.
""")

storageroom = room.Room("Storage Room", 
"""It looks like someone placed some black roses in here, but why?!
Also there are a few vegetables lying on the ground. 
It's quiet dark in here, a candle would be nice now...""")

hallway1 = room.Room("Hallway (west)", 
"""The hallway is almost empty.
There are just some pictures on the walls and an old carpet on the ground.""")

hallway2 = room.Room("Hallway (east)", 
"""This part of the hallway looks like the western part, except for the statue in the middle of the room.
It is a golden monument showing a crying child. """)

end = room.Room("Front of the House", "You finally made it out of the mansion!")

secret1 = room.Room("Hidden Room (ground floor)", """It seems like this room is empty...
But wait.. where does this sound come from? It sounds like a crying girl....""")

staircase = room.Staircase("Staircase (ground floor)", """An old wooden stair gives you access to the attic and the basement.
Some planks look like they're going to brake.
To the left of the room you see a luggage, but its locked..
""")

bedroom = room.Room("Bed Room", """"You are standing in a messy room. 
A bed is in the middle of the room.
You see blood on the blanket.""")

#floor 1
attic = room.Staircase("Attic", """An old wooden stair gives you access to the attic and the basement.
Some planks look like they're going to brake.""")

#floor 2
roof = room.Staircase("Roof", """You are standing on the roof. The garden is in the south. 
In the north you can see the city lights shining.""")

#floor -1
basement = room.Staircase("Basement", "There are a lot of shelves.")

secret2 = room.Room("Hidden Cave", "filler") #not used yet

#Define special items
BlackRose = items.Item("Black Rose", "One of the black roses you can find all over the house.", 0)