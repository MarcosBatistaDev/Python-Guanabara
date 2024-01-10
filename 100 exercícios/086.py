# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

matriz = []
dado = []
for c in range(0, 3):
    for v in range(0, 3):
        dado.append(int(input(f'Digite um valor para [{c}, {v}]: ')))
        matriz.append(dado[:])
        dado.clear()
print('-=-' * 13)
for c in range(0, 9):
    print(f"[{matriz[c][0]:^5}]", end=' ')
    if (c + 1) % 3 == 0:
        print()
print('-=-' * 13)