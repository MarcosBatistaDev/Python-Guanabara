# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

# Dados
valor_casa = float(input('Informe o valor do imóvel: R$'))
sal_comprador = float(input('Renda mensal: R$'))
anos_pagando = int(input('Em quantos anos pretende quitar o imóvel: '))

# Cálculos
preco_parcela = valor_casa / (anos_pagando * 12)
if preco_parcela > sal_comprador * 0.3:
    print(f'Empréstimo negado! Você ira pagar {anos_pagando * 12} parcelas de R${preco_parcela:.2f} em {anos_pagando} anos.')
    print('infelizmente não será possível financiar esta casa, você excedeu o limite de 30%.')
    
else:
    print(f'Empréstimo aprovado! Você ira pagar {anos_pagando * 12} parcelas de R${preco_parcela:.2f} em {anos_pagando} anos.')