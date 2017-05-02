### Item superclass
class Item():

    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
    
    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_value(self):
        return self.value



### Subclass of item: Coins asre ingame currency
class Coins(Item):
    def __init__(self, amount):
        self.amount = amount
        super().__init__(name="Coins", description = "Gather as much coins as you can! When you have enough you can buy cool new stuff", value = self.amount)



### Subclass of item: Weapons higher your AP(Attack Points)
class Weapon(Item):
    def __init__(self, name, description, value, ap):
        self.ap = ap
        super().__init__(name, description, value)

    def get_ap(self):
        return self.ap

### Subclass of weapon: your fist is the most basic weapon you can get
class Fist(Weapon):
    def __init__(self):
        super().__init__(name = "None", description = "Your most basic wepon", value = 0, ap = 1)

### Subclass of weapon: the wooden sword is a weak basic weapon
class WoodenSword(Weapon):
    def __init__(self):
        super().__init__(name = "Wooden Sword", description = "A weak basic weapon", value = 5, ap = 2)

### Subclass of weapon: a basic sword
class Sword(Weapon):
    def __init__(self):
        self.enchanted = enchanted
        super().__init__(name = "Sword", description = "A usual sword, neither good nor bad", value = 15, ap = 4+enchanted)

### Subclass of weapon: a basic sword
class BigSword(Weapon):
    def __init__(self):
        self.enchanted = enchanted
        super().__init__(name = "Sword", description = "A usual sword, neither good nor bad", value = 35, ap = 8)


### Subclass of Item: healing potion for exhausted players
class Potion(Item):
    def __init__(self, name, heal):
        self.heal = heal
        super().__init__(name = "Potion", description = "This potion heals you for " + self.heal + " HP" , value = 10)

    def get_heal(self):
        return self.heal

class SmallPotion(Potion):
    def __init__(self):
        super().__init__("Small Potion", 2)

class MediumPotion(Potion):
    def __init__(self):
        super.__init__("Medium Potion", 4)

class BigPotion(Potion):
    def __init__(self):
        super().__init__("Big Potion", 6)




        

