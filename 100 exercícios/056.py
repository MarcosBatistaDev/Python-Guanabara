# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

cont = 0
mulherMenor = 0
media = 0

for c in range(0, 4):
    if c == 0:
        homem_velho = ''
        idadeVelho = 0
    cont += 1
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo M/F: ')).strip().lower()
    if sexo == 'm' and idade > idadeVelho:
        idadeVelho = idade
        homem_velho = nome
    elif sexo == 'f' and idade < 20:
        mulherMenor += 1
    media += idade
media = media / cont

print(f'Média de idade do grupo: {media}')
print(f'Homem mais velho: {homem_velho} com {idadeVelho} anos de idade')
print(f'Mulheres com menos de 20 anos: {mulherMenor}')

