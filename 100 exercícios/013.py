# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input("Informe seu salário R$"))
aumento = (salario / 100 * 15)
print(f"Seu salário de R${salario:.2f} com 15% de aumento se tornará R${salario + aumento:.2f}")