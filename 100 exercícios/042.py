"""Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes"""

s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))

if s1 + s2 > s3 and s2 + s3 > s1 and s3 + s1 > s2:
    if s1 == s2 == s3:
        print('Os segmentos formam um triângulo equilátero.')
    elif s1 != s2 != s3 != s1:
        print('Os segmentos formam um triângulo escaleno.')
    else:
        print('Os segmentos formam um triângulo isósceles.')
else:
    print('Os segmentos não podem formar nenhum triângulo!')