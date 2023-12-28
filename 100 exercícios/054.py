# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

pessoas = list()
pessoas_maiores = list()

for c in range(0, 3):
    nome = str(input('Nome: ')).strip().title()
    ano_nasc = int(input('Data de nascimento: '))
    pessoas.append(nome)
    pessoas.append(ano_nasc)
    if date.today().year - ano_nasc >= 18:
        pessoas_maiores.append(nome)
        pessoas_maiores.append(date.today().year - ano_nasc)

print('-=-' * 8)
print(f'Ao todo são {len(pessoas) / 2:.0f} pessoas.')
print('-=-' * 8)
for c in range(0, len(pessoas) - 1, 2):
    print('--->', pessoas[c])
print('-=-' * 8)
print('Pessas maiores de idade')
for c in range(0, len(pessoas_maiores)):
    if c % 2 == 0:
        print(f'nome: {pessoas_maiores[c]}', end=' ')
    else:
        print(f'idade: {pessoas_maiores[c]}')
print('-=-' * 8)

