# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

media = 0
c = 0
maior = 0
menor = 0

while True:
    num = int(input('Digite um número: '))
    media += num
    c += 1
    if c == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    resp = str(input('Quer continuar [s/n]: ')).strip().lower()
    while resp != 's' and resp != 'n':
        resp = str(input('Quer continuar [s/n]: ')).strip().lower()
    if resp == 'n':
        break
print(f'Média: {media / c}')
print(f'Maior: {maior}')
print(f'Menor: {menor}')
print(c, media)