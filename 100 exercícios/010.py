# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

reais = float(input("Quanto tem na carteira R$"))
dolar = 4.94
print(f"Com R${reais:.2f} você pode comprar US${reais / dolar:.2f}")
