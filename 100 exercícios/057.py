# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Informe seu sexo [m/f]: ')).strip().lower()
while sexo != 'm' and sexo != 'f':
    print('Dados inválidos! Diigite novamente.')
    sexo = str(input('Informe seu sexo [m/f]: ')).strip().lower()
print(f'Sexo {sexo} registrado com sucesso!')
    