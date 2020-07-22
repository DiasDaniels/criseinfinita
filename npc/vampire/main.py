from npc.main import Npc
class Vampire(Npc):
    def __init__(self, hp, atk, arm):
        self.name = "Vampiro"
        super().__init__ (self.name, hp, atk, arm)