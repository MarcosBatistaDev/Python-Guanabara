"""Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:

0 – 1 – 1 – 2 – 3 – 5 – 8"""

num = int(input('Número de termos: '))
a = 0
b = 1
ab = 1
c = 0
while True:
    print(a, end=' -> ')
    c += 1
    ab = a + b
    a = b
    b = ab
    if c == num:
        break
print('Fim')