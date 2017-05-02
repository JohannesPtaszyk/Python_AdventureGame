### Enemy superclass for creating enemies
class Enemy:
    def __init__(self, name, hp, ap):
        self.name = name
        self.hp = hp
        self.ap = ap
    
    #get enemy name
    def get_name(self):
        return self.name

    #get enemy ap
    def get_ap(self):
        return self.ap

    #get enemy hp
    def get_hp(self):
        return self.hp
    
    #enemy hp - dmg
    def loose_hp(self, dmg):
       self.hp -= dmg
    
    #prove if enemy is alive. If enemy is alive return true otherwise return false
    def is_alive(self):
        if self.hp > 0:
            return True
        else:
            return False

### A Spider is a weak basic enemy
class Spider(Enemy):
    def __init__(self):
        super().__init__(name = "Spider", hp = 2, ap = 1)

### A Big Spider is a basic enemy
class BigSpider(Enemy):
    def __init__(self):
        super().__init__(name = "Big Spider", hp = 4, ap = 2)

### A Huge Spider is a stronger basic enemy
class HugeSpider(Enemy):
    def __init__(self):
        super().__init__(name = "Huge Spider", hp = 6, ap = 4)

### A Ghost is a strong enemy
class Ghost(Enemy):
    def __init__(self):
        super().__init__(name = "Ghost", hp = 8, ap = 8)

        
