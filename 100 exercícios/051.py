# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

termo = int(input('Termo da PA: '))
razao = int(input('Razão da PA: '))
for c in range(termo, termo + (razao * 10), razao):
    if c != termo + (razao * 9):
        print(c, end=' -> ')
    else:
        print(c, end=' Fim')