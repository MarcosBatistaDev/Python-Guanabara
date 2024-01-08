# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

numeros = list()
while True:
    temp = int(input('Digite um número: '))
    if temp in numeros:
        print('Número duplicado. Não vou adiocionar!')
    else:
        numeros.append(temp)
        print('Número adiconado com sucesso.')
    opc = str(input('Quer continuar (S/N): ')).strip().lower()
    while opc != 's' and opc != 'n':
        opc = str(input('Quer continuar (S/N): ')).strip().lower()
    if opc == 'n':
        break
print(f'Valores digitados: {sorted(numeros)}')