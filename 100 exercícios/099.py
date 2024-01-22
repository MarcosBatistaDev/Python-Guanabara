# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(*num):
    c = 0
    for n in num:
        if c == 0:
            maior_num = n
        else:
            if n > maior_num:
                maior_num = n
        c += 1
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'Recebi os valores {num} é o maior número lido foi {maior_num}.')

maior(10, 2, 3, 5, 6, 11, 2)
maior(4, 7, 0)
maior(1, 2)
maior(2, 9, 3, 5, 7, 1)