from  char import Char
class Player(Char):
    def __init__(self, name, hp, atk, arm):
        super().__init__ (name, hp, atk, arm)
        self.__score = 0
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

    def setScore(self,score:int):
        if score in [100, 300, 600, 1200, 2400, 4800]:
            print('Você subiu de nível! ATK + 10 || DEF + 5')
            self.atk += 10
            self.arm += 5

        else:
            print('Vocẽ recebeu', self.__score, 'de experiência!')
        self.__score = score

    def getScore(self):
        return self.__score
