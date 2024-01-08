# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

numeros = list()
pares = list()
impares = list()

while True:
    temp = int(input('Digite um número: '))
    numeros.append(temp)
    if temp % 2 == 0:
        pares.append(temp)
    else:
        impares.append(temp)
    resp = str(input('Quer continuar (S/N): ')).strip().lower()
    while resp != 's' and resp != 'n':
        resp = str(input('Quer continuar (S/N): ')).strip().lower()
    if resp == 'n':
        break
print('-=-' * 12)
print(f'Você digitou os valores: {numeros}')
print(f'Pares: {pares}')
print(f'Ímpares: {impares}')
print('-=-' * 12)

