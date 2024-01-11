"""Aprimore o desafio anterior, mostrando no final:                                                    A) A soma de todos os valores pares digitados.                                                                                                  B) A soma dos valores da terceira coluna.                                                                                                                C) O maior valor da segunda linha."""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = scol = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posicão [{l}, {c}]: '))
print('-=-' * 12)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end="")
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]

    print()
print('-=-' * 12)
print(f'A soma dos pares vale {spar}.')

for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna vale {scol}.')

for c in range(0, 3):
    if l == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha vale {maior}.')
