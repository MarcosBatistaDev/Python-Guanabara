# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

numeros = [[], []]
for v in range(0, 7):
    num = int(input('Valor: '))
    if num % 2 == 0:
        numeros[0].insert(v, num)
    else:
        numeros[1].insert(v, num)
print('-=-' * 16)
numeros[0].sort(reverse=False)
numeros[1].sort(reverse=False)
print(f'Os valores pares digitados foram: {numeros[0]}')
print(f'Os valores ímpares digitados foram: {numeros[1]}')
print('-=-' * 16)
