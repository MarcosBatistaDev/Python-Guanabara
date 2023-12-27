# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

print('Programa que só mostra valores pares.')
num = int(input('Informe o valor para ver seu pares: '))
for c in range(1, num + 1):
    if c % 2 == 0:
        print(c, end=' ')