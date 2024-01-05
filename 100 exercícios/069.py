"""Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos."""

maior_18 = homens = muMenor_20 = 0

print('-=-' * 14)
print("         Cadastro Nacional 1.0")
print('-=-' * 14)
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): ')).strip().lower()
    while sexo != 'm' and sexo != 'f':
        sexo = str(input('Sexo (M/F): ')).strip().lower()
    if idade > 18:
        maior_18 += 1
    if sexo == 'm':
        homens += 1
    elif sexo == 'f' and idade < 20:
        muMenor_20 += 1
    opc = str(input('Continuar? (S/N): ')).strip().lower()
    while opc != 's' and opc != 'n':
            opc = str(input('Continuar? (S/N): ')).strip().lower()
    if opc == 'n':
         break
    else:
         print('-=-' * 14)
         print("         Cadastro Nacional 1.0")
         print('-=-' * 14)
print('-=-' * 14)
print(f'quantas pessoas tem mais de 18 anos: {maior_18}')
print(f'quantos homens foram cadastrados: {homens}')
print(f'quantas mulheres tem menos de 20 anos: {muMenor_20}')
print('-=-' * 14)




         