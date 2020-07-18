from player.main import Player
from npc.main import Npc
from random import randint
from helpers import printWSleep
class Turn:
  def __init__(self,player:Player,npc:Npc):
    self.player = player
    self.npc = npc
    self.action()

  def action(self):
    playerAction = 0
    npcAction = int(randint(1,3))
    
    while str(playerAction) not in '12':
      print('Player HP: ',self.player.hp)
      print('Enemy HP: ',self.npc.hp)

      

      print('''Erga sua arma contra essa vil criatura ou defenda-se!
      [  1  ] Para atacar
      [  2  ] Para defender ''')
      playerAction = (str(input('Escolha uma opção: ')))

    if int(playerAction) == 2:
      self.player.defend = True
    if npcAction == 3:
      self.npc.defend = True

    if self.npc.defend and self.player.defend:
      self.player.turnHeal()
    if not self.player.defend:
      self.npc.calculateDamage(self.player.atk)
    if not(self.npc.defend) and self.npc.alive:
      self.player.calculateDamage(self.npc.atk)
    
    self.player.defend = False
    self.npc.defend = False
    printWSleep()
    
