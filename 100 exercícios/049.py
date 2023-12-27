# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

print('Tabuada 2.0')
num = int(input("Informe o valor para ver sua tabuada: "))
print('-=-' * 6)
for c in range(1, 11):
    print(f'{num:>2} x {c:>2} = {num * c:>3}')
print('-=-' * 6)