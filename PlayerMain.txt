class Player:
    def __init__(self, name, hp, atk, arm):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.arm = arm
        self.alive = True

    def losshp(self, vida):
        self.hp -= int(vida)
        print('Você tomou ', vida, ' de dano')
        if(self.hp < 1):
            print('Você morreu!')
            self.alive = False
        
    def defense(self, vida, arm):
        self.hp -= (int(vida) - int(arm))
        print('Você tomou ', (vida - arm), ' de dano')
        if(self.hp < 1):
            print('Você morreu! ☠')
            self.alive = False