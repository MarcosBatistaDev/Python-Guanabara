# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número: '))
cont = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[32m', end='')
        cont += 1
    else:
        print('\033[31m', end='')
    print(c, end=' ')
print('\033[35m')
if cont > 2:
    print(f'O numero {num} foi divisivel por {cont} números, portanto não é primo!')
else:
    print(f'O numero {num} foi divisivel por {cont} números, portanto é primo!')
print('\033[m', end='')