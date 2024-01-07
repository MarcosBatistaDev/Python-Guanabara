"""Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares."""

numero = (int(input('Digite um número: ')), int(input('Outro número: ')), int(input('Mais um número: ')), int(input('Último número: ')))
print(f'Você digitou os números: {numero}')
print(f'O valor 9 apareceu {numero.count(9)} vezes.')
print(f'{'O número 3 apareceu na posicão ' + str(numero.index(3)) if 3 in numero else 'O número 3 não foi digitado.'}')
print('Valores pares digitados: ', end='')
for c in numero:
    if c % 2 == 0:
        print(c, end=' ')