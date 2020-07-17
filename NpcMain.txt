class Npc:
    def __init__(self, name, hp, atk, arm):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.arm = arm
        self.alive = True

    def losshp(self, vida):
        self.hp -= int(vida)
        print(self.name, ' tomou ', vida, ' de dano')
        if(self.hp < 1):
            print(self.name, ' morreu!')
            self.alive = False

    def defense(self, vida, arm):
        self.hp -= (int(vida) - int(arm))
        print(self.name, (vida - arm), ' de dano')
        if(self.hp < 1):
            print(self.name, ' morreu!')
            self.alive = False