# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

medida = float(input("Media em metros: (M):"))
print(f"Valor em centímetros: {medida * 100:.0f}(cm)")
print(f'Valor em milímetros: {medida * 1000:.0f}(mm)')
