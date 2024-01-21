"""Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2 
c) uma contagem personalizada"""

from time import sleep

def linha(tam):
    print('-=-' * tam)

def contador(início, fim, passo):
    if passo == 0:
        passo = 1
    elif passo < 0:
        passo *= -1
    if início < fim:
        while início <= fim:
            print(início, end=' ', flush=True)
            sleep(0.2)
            início += passo
        print('Fim')
    
    elif início > fim:
        while início >= fim:
            print(início, end=" ", flush=True)
            sleep(0.2)
            início -= passo
        print('Fim')



# CONTAGEM 1 A 10
print('Contagem de 1 a 10 de 1 em 1')
linha(10)
contador(1, 10, 1)
linha(10)

# Contagem de 10 a 0 de 2 em 2
print('Contagem de 10 a 0 de 2 em 2')
linha(10)
contador(10, 0, 2)
linha(10)

# Contagem personalizada
print('Agora é sua vez de personalizar a contagem.')
linha(10)
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
linha(10)
contador(i, f, p)
linha(10)

