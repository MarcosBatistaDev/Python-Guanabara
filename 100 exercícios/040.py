""" Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: c

– Média 7.0 ou superior: APROVADO""" 

nota_1 = float(input('Nota 1: '))
nota_2 =  float(input('Nota 2: '))
media = (nota_1 + nota_2) / 2
if media < 5:
    print(f'Com média de {media} você está REPROVADO!')
elif media < 7:
    print(f'Com média de {media} você está de RECUPERAÇÃO!')
else:
    print(f'Com média de {media} você está APROVADO!')