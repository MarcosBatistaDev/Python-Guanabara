# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

num = int(input('Digite um número (999 para parar): '))
c = 0
soma = 0
while num != 999:
    c += 1
    soma += num
    num = int(input('Digite um número (999 para parar): '))
print(f'Ao todo foram {c} números e soma foi {soma}.')
