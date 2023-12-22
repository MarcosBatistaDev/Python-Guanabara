# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

pc_num = randint(0, 5)
user = int(input('Pensei em um número entre 0 e 5. Qual foi: '))
print('Verificando...')
sleep(0.7)
if user == pc_num:
    print(f'Você acertou! pensei no número {pc_num}')
else:
    print(f'Você errou :( pensei no número {pc_num}')