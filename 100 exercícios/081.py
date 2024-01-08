"""Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C)Se o valor 5 foi digitado e está ou não na lista."""

lista = list()
while True:
    lista.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar (S/N): ')).strip().lower()
    while resp != 's' and resp != 'n':
        resp = str(input('Quer continuar (S/N): ')).strip().lower()
    if resp == 'n':
        break
print('-=-' * 12)
print(f'Ao todo são {len(lista)} elementos.')
print(f'Lista decrescente: {sorted(lista, reverse=True)}')
print(f'O valor 5 apareceu na posicão {lista.index(5)}' if 5 in lista else "O valor 5 não foi digitado!")
print('-=-' * 12)

