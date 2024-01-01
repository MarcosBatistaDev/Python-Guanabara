# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

num = int(input('Primeiro Termo da PA: '))
razao = int(input('Razão da PA: '))
num_termos = int(input('Número de termos: '))
print('-=-' * 20)
while True:
    print(num, end=' ')
    print(end='-> ' if num_termos > 1 else ' Fim')
    num += razao
    num_termos -= 1
    if num_termos == 0:
        print()
        break
print('-=-' * 20)
