"""Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato"""

prod_barato = str()
preco_barato = 0
prods_1000 = 0
tot = 0
c = 0

while True:
    produto = str(input('Produto: ')).strip().title()
    preco = float(input('Preco do produto: R$'))
    if preco > 1000:
        prods_1000 += 1
    if c == 0:
        preco_barato = preco
        prod_barato = produto
    elif preco < preco_barato:
        preco_barato = preco
        prod_barato = produto

    tot += preco
    c += 1
    resp = str(input('Quer continuar (S/N): ')).strip().lower()
    while resp != 's' and resp != 'n':
        resp = str(input('Quer continuar (S/N): ')).strip().lower()
    if resp == 'n':
        break


print(f'Total gasto na compra: R${tot:.2f}')
print(f'Total de produtos que custa + de R$1000: {prods_1000}')
print(f'Nome do produto mais barato: {prod_barato} preco: R${preco_barato:.2f}')