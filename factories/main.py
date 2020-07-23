from npc.goblin.main import Goblin
from npc.ogre.main import Ogre
from npc.vampire.main import Vampire
from npc.succubus.main import Succubus
from random import randint
from player.main import Player


def makeGoblin(score: int):
    goblinhp = 80
    baseAtk = 8 + (5 * score) + 1
    maxAtk = 13 + (5 * score) + 1
    goblinatk = randint(baseAtk, maxAtk)
    baseArm = 5 + (3 * score) + 1
    maxArm = 9 + (3 * score) + 1
    goblinarm = randint(baseArm, maxArm)
    return Goblin(goblinhp, goblinatk, goblinarm)


def makeOgre(score: int):
    ogrehp = 100
    baseAtk = 7 + (6 * score) + 2
    maxAtk = 13 + (6 * score) + 2
    ogreatk = randint(baseAtk, maxAtk)
    baseArm = 5 + (3 * score) + 2
    maxArm = 9 + (3 * score) + 1
    ogrearm = randint(baseArm, maxArm)
    return Ogre(ogrehp, ogreatk, ogrearm)


def makeVampire(score: int):
    vampirehp = 280
    baseAtk = 10 + (6 * score) + 2
    vampireatk = baseAtk
    baseArm = 16 + (3 * score) + 1
    vampirearm = baseArm
    return Vampire(vampirehp, vampireatk, vampirearm)

def makeSuccubus(score: int):
    succubushp = 280
    baseAtk = 10 + (6 * score) + 2
    succubusatk = baseAtk
    baseArm = 16 + (3 * score) + 1
    succubusarm = baseArm
    return Succubus(succubushp, succubusatk, succubusarm)


def makePlayer(name: str, classe: int):
    if classe == 1:
        hp = 100
        atk = 15
        arm = 10
    elif classe == 2:
        hp = 1000
        atk = 50
        arm = 8
    else:
        hp = 100
        atk = 8
        arm = 15

    return Player(name, hp, atk, arm)


def makeNpc(score: int):
    if score % 5 == 0 and score != 0:
        selektor = ['Vampiro', 'Succubus']
        choose = randint(0, len(selektor) - 1)
        if selektor [choose] == 'Vampiro':
            return makeVampire(score)
        if selektor [choose] == 'Succubus':
            return makeSuccubus(score)
    else:
        selector = ["Goblin", "Ogro"]
        choose = randint(0, len(selector) - 1)
        if selector[choose] == 'Goblin':
            return makeGoblin(score)
        if selector[choose] == 'Ogro':
            return makeOgre(score)