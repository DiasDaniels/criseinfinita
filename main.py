from player.main import Player
from npc.main import Npc
from time import sleep
from random import randint, random
def separador():
    print('||✝'*30)
goblinhp = 80
goblinatk = randint(8, 13)
goblinarm = randint(5, 9 )
mon = Npc('Goblin', goblinhp, goblinatk, goblinarm)
separador()
print(f'''{'Boas vindas à "Crise Infinita Infinita Infinita.':.^30}
{'Você irá batalhar infinitamente, até cansar ou morrer.':.^30}
{'Vamos começar com o básico.':.^30}''')
separador()
artigo = []
name = (input(str("Qual é o seu nome, Aventureiro? "))).strip().capitalize()
arma = ''
hp = 100
atk = 10
arm = 8
monkilled = 0
bosskilled = 0
j1 = Player(name, hp, atk, arm)

separador()
print('''    Qual será sua arma?:
    [  1  ] Espada
    [  2  ] Lança
    [  3  ] Machado''')
opt = int(input('Digite uma opção: '))
if opt == 1:
    separador()
    print('Você escolheu a Espada, prepare-se!')
    arma = 'Espada'
if opt == 2:
    separador()
    print('Você escolheu a Lança, prepare-se!')
    arma = 'Lança'
if opt == 3:
    separador()
    print('Você escolheu o Machado, prepare-se!')
    arma = 'Machado'

if(arma =='Machado'):
    artigo = ['um','seu']
else:
    artigo = ['uma','sua']
separador()


print (f'''Durante uma tempestade de gafanhotos, {j1.name} procurava um lugar para se abrigar, ouviu um chamado abaixo de uma ponte que cruzava um córrego
um velho homem fedorento que tinha com ele algumas trouxas, umas de roupas e outras de sabe-se Odin lá o que. Após um diálogo breve, o mendigo, ausente de suas
faculdades mentais, te entrega {artigo[0]} {arma}, você segue seu caminho após a tempestade de gafanhotos e, ao final da ponte, você encontra um Goblin sedento
por sangue.
Prepare-se para usar {artigo[1]} {arma}!''')
for i in range(9):
    sleep(1)
    print('.', end= " ", flush= True)
sleep(1)
print('.')

separador()
while j1.alive:
    print(f'Um {mon.name} apareceu! Prepare-se!')
    for i in range(9):
        sleep(0.25)
        print('=', end= " ", flush= True)
    print('=')
    while j1.alive and mon.alive:
        monchoose = str(randint(1,2))
        print('''Erga sua arma contra essa vil criatura ou defenda-se!
        [  1  ] Para atacar
        [  2  ] Para defender ''')
        batchoose = (str(input('Escolha uma opção: ')))
        if monchoose in '1' and batchoose in '1':
            j1.losshp(mon.atk)
            sleep(2)
            if not j1.alive:
                break
            print (f'Você está com {j1.hp} de HP.')   
            mon.losshp(j1.atk)
            sleep(2)
            if not mon.alive:
                monkilled += 1
                goblinhp += 5
                mon = Npc(mon.name, goblinhp, mon.atk +3, 0)
                print('='*15)
                break
            else:
                print (f'{mon.name} está com {mon.hp} de HP.')
        if monchoose in '1' and batchoose in '2':
            j1.defense(mon.atk, j1.arm)
            sleep(2)
            if not j1.alive:
                break
            print (f'Você está com {j1.hp} de HP.')  
            print (f'{mon.name} está com {mon.hp} de HP.')
        if monchoose in '23' and batchoose in '1':
            mon.defense(j1.atk, mon.arm)
            sleep(2)
            if not mon.alive:
                monkilled += 1
                goblinhp += 5
                mon = Npc(mon.name, goblinhp, mon.atk +3, 0)
                print('='*15)
                break
            print (f'Você está com {j1.hp} de HP.')
            print (f'{mon.name} está com {mon.hp} de HP.')
        if monchoose in '23'  and batchoose in '2':
            sleep(2)
            j1.hp += 10
            print(f'Você ganhou +10HP')
            print (f'Você está com {j1.hp} de HP.')
            print (f'{mon.name} está com {mon.hp} de HP.')
        for i in range(9):
            sleep(0.25)
            print('=', end= " ", flush= True)
        print('=')

    if not j1.alive:
        break

print(f'Fim de jogo, você fez {monkilled * 100} pontos!')


