# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date

registro_pessoa = dict()
registro_pessoa['nome'] = str(input('Nome: ')).strip().title()
registro_pessoa['ano de nascimento'] = int(input('Ano de nascimento: '))
registro_pessoa['idade'] = date.today().year - registro_pessoa['ano de nascimento']
registro_pessoa['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if registro_pessoa['ctps'] != 0:
    registro_pessoa['ano de contratação'] = int(input('Ano de contratação: '))
    registro_pessoa['salário'] = float(input('Salário: '))
    registro_pessoa['aposentadoria'] = (registro_pessoa['ano de contratação'] + 35) - registro_pessoa['ano de nascimento']

print('-=-' * 14)
for k, v in registro_pessoa.items():
    print(f'---- {k} tem valor {v}.')

