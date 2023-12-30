# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep


pc_num = randint(0, 10)
cont = 0

print('-=-' * 10)
print('Jogo da adivinhacão V2.0')
print('-=-' * 10)
print('Vou pensar em número entre 0 e 10...')
sleep(1)
print('-' * 15)
print('Pensando...')
print('-' * 15)
sleep(2)
num = int(input('Em qual número eu pensei: '))
cont += 1

while num != pc_num:
    print('-' * 25)
    print('Nop, tente outro número')
    print('-' * 25)
    num = int(input('Em qual número eu pensei: '))
    sleep(1)
    cont += 1

print('-' * 25)
print('Parabéeeeens, você acertou!!!')
print(f'Número de tentativas: {cont}')
print('-' * 25)