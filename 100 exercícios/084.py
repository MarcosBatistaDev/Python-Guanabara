"""Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:                                                   A) Quantas pessoas foram cadastradas.                                              B) Uma listagem com as pessoas mais pesadas.                                                  C) Uma listagem com as pessoas mais leves."""

pessoas = list()
dados = list()
maiorPeso = menorPeso = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maiorPeso = menorPeso = dados[1]
    else:
        if dados[1] > maiorPeso:
            maiorPeso = dados[1]
        elif dados[1] < menorPeso:
            menorPeso = dados[1]
        
    pessoas.append(dados[:])
    resp = str(input('Quer continuar (S/N): ')).strip().lower()
    while resp != 's' and resp != 'n':
        resp = str(input('Quer continuar (S/N): ')).strip().lower()
    if resp == 'n':
        break
    dados.clear()
print(f'Ao todo foram {len(pessoas)} pessoas cadastradas. ')
print(f'O maior peso lido foi de {maiorPeso:.1f}. Peso de', end=" ")
for p in pessoas:
    if p[1] == maiorPeso:
        print(p[0], end=" ")
print(f'\nO menor peso lido foi de {menorPeso:.1f}Kg. Peso de ', end="")
for p in pessoas:
    if p[1] == menorPeso:
        print(p[0], end=' ')
