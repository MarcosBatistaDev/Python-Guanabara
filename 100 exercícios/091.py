# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from operator import itemgetter
from time import sleep

jogos = dict()
jogos['jogador_1'] = randint(1, 6)
jogos['jogador_2'] = randint(1, 6)
jogos['jogador_3'] = randint(1, 6)
jogos['jogador_4'] = randint(1, 6)
ranking = list()
ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)
print('Valores sorteados')
for k, v in jogos.items():
    print(f'{k} tirou {v}')
    sleep(1)
print(' == Ranking de jogadores == ')
for i,v in enumerate(ranking):
    print(f'    {i+1} lugar está o {v[0]} com {v[1]} pontos.')
    sleep(1)