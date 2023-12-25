"""Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal 

– 3x ou mais no cartão: 20% de juros"""

nome_produto = str(input('Nome do produto: ')).strip().title()
preco_produto = float(input('Preco do produto: R$'))
tipo_pagamento = int(input("""Tipo de pagamento:
[1] à vista dinheiro/cheque: 10% de desconto
[2] à vista no cartão: 5% de desconto
[3] em até 2x no cartão: preço formal
[4] 3x ou mais no cartão: 20% de juros
sua escolha: """))

if tipo_pagamento == 1:
    print(f'Você pagará o valor de R${preco_produto - (preco_produto * 0.1):.2f} no produto: {nome_produto}')
elif tipo_pagamento == 2:
    print(f'Você pagará o valor de R${preco_produto - (preco_produto * 0.05):.2f} no produto: {nome_produto}')
elif tipo_pagamento == 3:
    print(f'Serão 2 parcelas de R${preco_produto / 2:.2f} no produto: {nome_produto}')
elif tipo_pagamento == 4:
    num_parcelas = int(input('Quantas vezes deseja parcelar: '))
    if num_parcelas == 0:
        print('Escolha inválida!')
    elif num_parcelas == 1:
        print(f'Você pagará o valor de R${preco_produto - (preco_produto * 0.05):.2f} no produto: {nome_produto}')
    else:
        print(f'Você irá pagar {num_parcelas} parcelas de R${(preco_produto + (preco_produto * 0.2)) / num_parcelas:.2f} (20% de juros).')
else:
    print('Escolha inválida!')