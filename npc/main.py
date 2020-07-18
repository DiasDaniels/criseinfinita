class Npc:
    def __init__(self, name, hp, atk, arm):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.arm = arm
        self.alive = True
        self.defend = False

    def __losshp(self, dmg):
        self.hp -= int(dmg)
        print(self.name, ' tomou ', dmg, ' de dano')
        print( self.name, ' está com ', self.hp, ' de HP')
        self.__amIDead()        

    def __defense(self, dmg):
        self.__losshp(int(dmg) - int(self.arm))
    
    def __amIDead(self):
        if(self.hp < 1):
            print(f'{self.name} morreu! ☠')
            self.alive = False

    def calculateDamage(self,dmg):
        if(not self.defend):
             self.__losshp(dmg)
        if(self.defend):
            self.__defense(dmg)    