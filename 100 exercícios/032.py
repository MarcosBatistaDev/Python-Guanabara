# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date

ano = int(input('Informe o ano atual (0 para ver o ano atual): '))
if ano == 0:
    ano = date.today().year
print(f'Analisando o ano de {ano}')
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Este ano com certeza é BISSEXTO!')
else:
    print('Este ano NÃO é BISSEXTO!')