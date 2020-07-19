from  char import Char
class Player(Char):
    def __init__(self, name, hp, atk, arm):
        super().__init__ (name, hp, atk, arm)
        self.setCallableName('Você')
    
    def turnHeal(self):
        if self.hp < 100:
            self.hp += 10
            if self.hp > 100:
                self.hp = 100
            print(f'Você ganhou +10HP')
            print(f'Você está com ',self.hp,' de HP')

        else:
            print('Você está descansado, vida Máxima atingida!')

