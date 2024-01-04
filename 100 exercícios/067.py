# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True:
    num = int(input('Digite um número para ver sua tabuada: '))
    if num < 0:
        break
    print('-=-' * 14)
    for c in range(1, 11):
        print(f'{num:>3} x {c:>3} = {num * c:>3}')
    print('-=-' * 14)
print('-=-' * 14)
print('Fim do programa Tabuada v3.0')
print('-=-' * 14)
