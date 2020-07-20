from npc.main import Npc
class Ogre(Npc):
    def __init__(self, hp, atk, arm):
        self.name = "Ogro"
        super().__init__ (self.name, hp, atk, arm)
       