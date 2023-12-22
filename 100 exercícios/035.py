# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))

if s1 + s2 > s3 and s2 + s3 > s1 and s3 + s1 > s2:
    print('Os segmentos a seguir podem sim formar um triângulo')
else:
    print('Os segmentos a seguir não podem formar um triângulo!')