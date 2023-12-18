# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

celsius = float(input("Informe a temperatura em C "))
formula = celsius * 1.8 + 32
print(f"A temperatura C {celsius:.1f} equivale a F {formula:.1f}")