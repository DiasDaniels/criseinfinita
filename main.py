from player.main import Player
from npc.goblin.main import Goblin
from time import sleep
from random import randint, random
from battle import Battle
import helpers
from factories.main import makeGoblin, makePlayer

helpers.separador()


helpers.separador()
print(f'''{'Boas vindas à "Crise Infinita Infinita Infinita.':.^30}
{'Você irá batalhar infinitamente, até cansar ou morrer.':.^30}
{'Vamos começar com o básico.':.^30}''')
helpers.separador()
artigo = []
name = (input(str("Qual é o seu nome, Aventureiro? "))).strip().capitalize()
arma = ''
monkilled = 0
bosskilled = 0
j1 = makePlayer(name)
mon = makeGoblin(monkilled)

helpers.separador()
opt = 0
print('''    Qual será sua arma?:
    [  1  ] Espada
    [  2  ] Lança
    [  3  ] Machado''')
while int(opt) not in [1, 2, 3]:
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
        j1.setScore (monkilled * 100)
        mon = makeGoblin(monkilled)

print('Fim de jogo, você fez', j1.getScore(), 'pontos!')
