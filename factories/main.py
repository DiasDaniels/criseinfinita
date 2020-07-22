from npc.goblin.main import Goblin
from npc.ogre.main import Ogre
from npc.vampire.main import Vampire
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


def makePlayer(name: str, classe: int):
    if classe == 1:
        hp = 100
        atk = 15
        arm = 10
    elif classe == 2:
        hp = 100
        atk = 40
        arm = 8
    else:
        hp = 100
        atk = 8
        arm = 15

    return Player(name, hp, atk, arm)


def makeNpc(score: int):
    selector = ["Goblin", "Ogro","Vampiro"]
    choose = randint(0, len(selector) - 2)
    if score % 5 == 0 and score != 0:
        selector = 'Vampiro'
        return makeVampire(score)
    else:
        if selector[choose] == 'Goblin':
            return makeGoblin(score)
        if selector[choose] == 'Ogro':
            return makeOgre(score)