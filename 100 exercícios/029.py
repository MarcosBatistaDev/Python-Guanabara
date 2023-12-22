# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

vel = float(input('Informe a velocidade do veículo (km/h):'))
if vel > 80:
    print(f'Você excedeu o limite de velocidade e foi multado no valor de R${(vel - 80) * 7:.2f}')
print('Tenha um bom dia, dirija com segurança!')