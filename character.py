class character:
    def __init__(self,name,health=20,attack=5,defense=5):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        
    def health_increase(self,inc=1):
        self.health += inc
    def attack_increase(self,inc=1):
        self.attack += inc
    def def_increase(self,inc=1):
        self.defense += inc
        
    