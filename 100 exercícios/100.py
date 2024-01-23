# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint
from time import sleep

num_sorteados = list()

def sorteia(lista):
    print('Números sorteados: ', end='')
    for c in range(0, 5):
        n = randint(0, 10)
        lista.append(n)
        print(f'{n}', end=' ', flush=True)
        sleep(0.3)
    print('Fim')

def somaPar(lista):
    s = 0
    for valor in lista:
        if valor % 2 == 0:
            s += valor
    print(f'Somando os valores pares de {lista} temos um total de {s}.')


sorteia(num_sorteados)
somaPar(num_sorteados)
