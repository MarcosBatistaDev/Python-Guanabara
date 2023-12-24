""" Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais """

num_1 = int(input('Primeiro número: '))
num_2 = int(input('Segundo número: '))

if num_1 > num_2:
    print('O Primeiro valor é maior')
elif num_2 > num_1:
    print('O Segundo valor é maior')
else:
    print('Os dois valores são iguais')
