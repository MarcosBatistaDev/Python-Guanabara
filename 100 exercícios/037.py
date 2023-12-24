# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:')
print("""[1] converter para binário
[2] converter para octal
[3] converter para hexadecimal""")
opc = int(input('Sua escolha: '))
if opc == 1:
    print(f"{num} para binário se torna {bin(num)[2:]}")
elif opc == 2:
    print(f"{num} para octal se torna {oct(num)[2:]}")
elif opc == 3:
    print(f"{num} para hexadecimal se torna {hex(num)[2:]}")
else:
    print('Escolha inválida!')