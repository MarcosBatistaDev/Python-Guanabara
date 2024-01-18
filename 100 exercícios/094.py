# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média.

pessoas = list()
pessoa = dict()
idades = 0

while True:
    pessoa['nome'] = str(input('Nome: ')).strip().title()
    pessoa['sexo'] = str(input('Sexo (M/F): ')).strip().lower()
    while pessoa['sexo'] != 'm' and pessoa['sexo'] != 'f':
        print('Digite apenas M ou F.')
        pessoa['sexo'] = str(input('Sexo (M/F): ')).strip().lower()
    pessoa['idade'] = int(input('Idade: '))
    idades += pessoa['idade']
    pessoas.append(pessoa.copy())
    pessoa.clear()
    resp = str(input('Quer continuar (S/N): ')).strip().lower()
    while resp != 's' and resp != 'n':
        print('Digite apenas S ou N.')
        resp = str(input('Quer continuar (S/N): ')).strip().lower()
    if resp == 'n':
        break
print(f'A) Ao todo são {len(pessoas)} pessoas cadastradas.')
print(f'B) A média é de {idades / len(pessoas):.1f} anos.')
print(f'C) As mulheres cadastradas foram:', end=' ')
for v in pessoas:
    if v['sexo'] == 'f':
        print(v['nome'], end=' ')
print()
print('D) Lista das pessoas que estão acima de média:')
for e in pessoas:
    if e['idade'] > idades / len(pessoas):
        print(f'    -- nome == {e['nome']}; sexo == {e['sexo']}; idade == {e['idade']}')
print('<< ENCERRADO >>')