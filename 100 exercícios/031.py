# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

dist = float(input('Distância da sua viagem? (km):'))
if dist <= 200:
    preco_v = dist * 0.5
else:
    preco_v = dist * 0.45
    print('Você recebeu um desconto!!')
print(f'O preco da sua passagem para uma viagem de {dist:.1f}Km será de R${preco_v:.2f}')