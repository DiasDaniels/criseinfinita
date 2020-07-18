class Player:
    def __init__(self, name, hp, atk, arm):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.arm = arm
        self.alive = True
        self.defend = False

    def __losshp(self, dmg):
        self.hp -= int(dmg)
        print('Você tomou ', dmg, ' de dano')
        print('Você está com ', self.hp, ' de HP')
        self.__amIDead()
        
    def __defense(self, dmg):
        self.__losshp(int(dmg) - int(self.arm))

    def __amIDead(self):
        if(self.hp < 1):
            print('Você morreu! ☠')
            self.alive = False 

    def calculateDamage(self,dmg):
        if(not self.defend):
            self.__losshp(dmg)
        if(self.defend):
            self.__defense(dmg)
    
    def turnHeal(self):
        if self.hp < 100:
            self.hp += 10
            print(f'Você ganhou +10HP')
            print(f'Você está com ',self.hp,' de HP')
        else:
            print('Você está descansado, vida Máxima atingida!')

