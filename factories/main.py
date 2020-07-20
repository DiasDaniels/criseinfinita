from npc.goblin.main import Goblin
from random import randint
def makeGoblin(score:int):
    goblinhp = 80
    baseAtk = 8 + (5*score) 
    maxAtk = 13 + (5*score)
    goblinatk = randint(baseAtk, maxAtk)
    baseArm = 5 + (5*score)
    maxArm =9 + (5*score)
    goblinarm = randint(baseArm, maxArm )
    return Goblin( goblinhp, goblinatk, goblinarm)