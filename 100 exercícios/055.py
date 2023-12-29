# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

nome = str(input('Nome: '))
peso = float(input('Peso (kg):'))

maior_peso = peso
menor_peso = peso
nome_maior = nome
nome_menor = nome

for c in range(0, 2):
    nome = str(input('Nome: '))
    peso = float(input('Peso (kg):'))
    if peso > menor_peso:
        maior_peso = peso
        nome_maior = nome
    elif peso < menor_peso:
        menor_peso = peso
        nome_menor = nome
print(f'O menor peso lido foi de {nome_menor} com {menor_peso:.1f}kg')
print(f'O maior peso lido foi de {nome_maior} com {maior_peso:.1f}kg')
