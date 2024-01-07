# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('Caderno', 'Prateleira', 'Anhanguera', 'Piedade', 'Descanso')
for palavra in palavras:
    print(f'A palavra {palavra} tem as vogais: ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=" ")
    print()