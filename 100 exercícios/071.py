"""Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1."""

valor = int(input('Valor a ser sacado: R$'))
valor_50 = valor // 50
valor -= (valor_50 * 50 )
valor_20 = valor // 20
valor -= (valor_20 * 20)
valor_10 = valor // 10
valor -= (valor_10 * 10)
valor_1 = valor // 1
valor -= valor * 1

print(f'Notas 50: {valor_50}')
print(f'Notas 20: {valor_20}')
print(f'Notas 10: {valor_10}')
print(f'Notas 1: {valor_1}')