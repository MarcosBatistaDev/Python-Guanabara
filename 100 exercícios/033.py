# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
n3 = int(input("Digite um número: "))
maior = n1
menor = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
print(f'O menor foi {menor}')
print(f'O maior foi {maior}')
