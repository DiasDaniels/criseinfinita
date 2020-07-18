from player.main import Player
from npc.main import Npc
from time import sleep
from turn import Turn
from helpers import printWSleep
class Battle:
  def __init__(self, player:Player, npc:Npc):
    self.player = player
    self.npc = npc
    self.turns = 0
    self.__fight()
  def __fight(self):
    print(f'Um {self.npc.name} apareceu! Prepare-se!')
    printWSleep()
    while self.player.alive and self.npc.alive:
      self.turns += 1
      Turn(self.player,self.npc)
      