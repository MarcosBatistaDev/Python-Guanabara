"""Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120"""

print('-=-' * 10)
print('Programa que calcula fatorial')
print('-=-' * 10)
num = int(input('Digite um número: '))
print('-=-' * 10)
fator = num
fatorado = num

print(f'{fator}! =', end=' ')
while True:
    if fator >= 2:
        print(f'{fator} x', end=' ')
        fator -= 1
        fatorado *= fator
    else:
        print(f'1 = {fatorado}')
        print('-=-' * 10)
        break
    