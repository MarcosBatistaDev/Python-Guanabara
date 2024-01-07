# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print('Números sorteados: ', end='')
for n in numeros:
    print(n, end=' ')
print(f'\nMaior número: {max(numeros)}')
print(f'Menor número: {min(numeros)}')