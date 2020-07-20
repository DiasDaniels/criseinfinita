from npc.main import Npc
class Goblin(Npc):
    def __init__(self, hp, atk, arm):
        self.name = 'Goblin'
        super().__init__ (self.name, hp, atk, arm)
        #TODO-Corrigir bug dano negativo       
