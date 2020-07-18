from player.main import Player
from npc.main import Npc
from time import sleep
from random import randint, random
from battle import Battle
import helpers

helpers.separador()

goblinhp = 80
baseAtk = 8 
maxAtk = 13
goblinatk = randint(baseAtk, maxAtk)
baseArm = 5
maxArm =9
goblinarm = randint(baseArm, maxArm )
mon = Npc('Goblin', goblinhp, goblinatk, goblinarm)
helpers.separador()
print(f'''{'Boas vindas à "Crise Infinita Infinita Infinita.':.^30}
{'Você irá batalhar infinitamente, até cansar ou morrer.':.^30}
{'Vamos começar com o básico.':.^30}''')
helpers.separador()
artigo = []
name = (input(str("Qual é o seu nome, Aventureiro? "))).strip().capitalize()
arma = ''
hp = 100
atk = 10
arm = 8
monkilled = 0
bosskilled = 0
j1 = Player(name, hp, atk, arm)

helpers.separador()
opt = 0
print('''    Qual será sua arma?:
    [  1  ] Espada
    [  2  ] Lança
    [  3  ] Machado''')
while str(opt) not in "123":
    opt = int(input('Digite uma opção: '))
if opt == 1:
    helpers.separador()
    print('Você escolheu a Espada, prepare-se!')
    arma = 'Espada'
if opt == 2:
    helpers.separador()
    print('Você escolheu a Lança, prepare-se!')
    arma = 'Lança'
if opt == 3:
    helpers.separador()
    print('Você escolheu o Machado, prepare-se!')
    arma = 'Machado'

if(arma =='Machado'):
    artigo = ['um','seu']
else:
    artigo = ['uma','sua']
helpers.separador()


print (f'''Durante uma tempestade de gafanhotos, {j1.name} procurava um lugar para se abrigar, ouviu um chamado abaixo de uma ponte que cruzava um córrego
um velho homem fedorento que tinha com ele algumas trouxas, umas de roupas e outras de sabe-se Odin lá o que. Após um diálogo breve, o mendigo, ausente de suas
faculdades mentais, te entrega {artigo[0]} {arma}, você segue seu caminho após a tempestade de gafanhotos e, ao final da ponte, você encontra um Goblin sedento
por sangue.
Prepare-se para usar {artigo[1]} {arma}!''')

helpers.separador10s()

helpers.separador()
while j1.alive:

    Battle(j1,mon)
    if(j1.alive):
        monkilled += 1
        
        goblinhp += 10
        mon.hp = goblinhp
        
        baseAtk += 5
        maxAtk +=5
        mon.atk = randint(baseAtk,maxAtk)

        baseArm += 5
        maxArm +=5
        mon.arm = randint(baseArm,maxArm)
        mon.alive = goblinarm
        mon.alive = True

print(f'Fim de jogo, você fez {monkilled * 100} pontos!')


