# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

numeros = list()
for c in range(0, 5):
    t = int(input('Digite um número: '))
    if c == 0 or t > numeros[-1]:
        numeros.append(t)
        print('Valor adicionado ao fim da lista')
    else:
        pos = 0
        while pos < len(numeros):
            if t <= numeros[pos]:
                numeros.insert(pos, t)
                print(f'Número adicionado na posicão {pos}')
                break
            pos += 1
print(numeros)