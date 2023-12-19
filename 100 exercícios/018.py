# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import cos, tan, sin, radians

angulo = float(input("Digite um ângulo: "))
angulo = radians(angulo)

print(f"Cosseno = {cos(angulo):.2f}")
print(f"Seno = {sin(angulo):.2f}")
print(f"Tangente = {tan(angulo):.2f}")

