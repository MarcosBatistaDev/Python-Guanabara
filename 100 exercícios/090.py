# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

boletim = dict()

boletim['nome'] = str(input('Nome: ')).strip().title()
boletim['media'] = float(input('Média: '))
if boletim['media'] < 5:
    boletim['situacão'] = 'Reprovado'
elif boletim['media'] < 7:
    boletim['situacão'] = 'Recuperacão'
else:
    boletim['situacão'] = 'Aprovado'

for k, v in boletim.items():
    print(f'   - {k} é igual a {v}')