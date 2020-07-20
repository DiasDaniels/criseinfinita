from npc.goblin.main import Goblin
from npc.ogre.main import Ogre
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

def makeOgre(score:int):
    ogrehp = 100
    baseAtk = 7 + (6*score) + 2
    maxAtk = 13 + (6*score) + 2
    ogreatk = randint (baseAtk, maxAtk)
    baseArm = 5 + (6*score) + 2
    maxArm = 9 + (6*score) + 2
    ogrearm = randint(baseArm, maxArm)
    return Ogre(ogrehp, ogreatk, ogrearm)

def makePlayer(name:str):
    hp = 100
    atk = 15
    arm = 10
    return Player(name, hp, atk, arm)

def makeNpc(score:int):
    selector = ["Goblin","Ogro"]
    choose = randint(0, len(selector)-1)
    if selector[choose] == 'Goblin':
        return makeGoblin(score)
    if selector[choose] == 'Ogro':
        return makeOgre(score)


