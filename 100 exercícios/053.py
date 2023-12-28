"""Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA."""

frase = str(input('Digite uma frase: ')).lower().strip()
temp = ''
for c in range(len(frase) - 1, -1, -1):
    if frase[c] != ' ': 
        temp += frase[c]

print(f'A frase {frase} invertida fica {temp}.')
if frase.replace(' ', '') == temp:
    print('Portanto é um palíndromo!')
else:
    print('Portanto não é um palíndromo!')