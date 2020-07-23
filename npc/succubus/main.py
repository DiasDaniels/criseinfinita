from npc.main import Npc
class Succubus(Npc):
    def __init__(self, hp, atk, arm):
        self.name = "Succubus"
        super().__init__ (self.name, hp, atk, arm)