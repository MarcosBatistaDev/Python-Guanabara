#Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

num = int(input("Digite um número: "))
print("=" * 22)
for c in range(1, 11):
    print(f"{num:>3} x {c:>3} = {num * c:>3}")
print("=" * 22)