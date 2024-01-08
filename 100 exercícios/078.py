# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

numeros = list()
for c in range(0, 5):
    numeros.append(int(input('Digite um número: ')))
print(f'Você digitou os valores: {numeros}')
print(f'O maior valor foi {max(numeros)} nas posicões: ', end=' ')
for c, p in enumerate(numeros):
    if p == max(numeros):
        print(c, end='...')
print(f'\nO menor valor foi {min(numeros)} nas posicões: ', end=' ')
for c, p in enumerate(numeros):
    if p == min(numeros):
        print(c, end='...')