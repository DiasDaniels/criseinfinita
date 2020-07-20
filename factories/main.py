from npc.goblin.main import Goblin
from random import randint
from player.main import Player
def makeGoblin(score:int):
    goblinhp = 80
    baseAtk = 8 + (5*score) 
    maxAtk = 13 + (5*score)
    goblinatk = randint(baseAtk, maxAtk)
    baseArm = 5 + (5*score)
    maxArm =9 + (5*score)
    goblinarm = randint(baseArm, maxArm )
    return Goblin( goblinhp, goblinatk, goblinarm)

def makePlayer(name:str):
    hp = 100
    atk = 10
    arm = 8
    return Player(name, hp, atk, arm)

def makeNpc(score:int):
    selector = ["Goblin"]
    choose = randint(0, len(selector))
    if selector[choose] == 'Goblin':
        return makeGoblin(score)

