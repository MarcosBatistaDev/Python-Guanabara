# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

boletim = list()
aluno = list()

while True:
    aluno.append(str(input('Nome: ')).strip().title())
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))
    boletim.append(aluno[:])
    aluno.clear()
    resp = str(input('Quer continuar (S/N): ')).strip().lower()
    while resp != 's' and resp != 'n':
        resp = str(input('Quer continuar (S/N): ')).strip().lower()
    if resp == 'n':
        break
print('-=-' * 14)
print('{:<3} {:<9} {:^5}'.format('No.', 'Nome', 'Média'))
for c, v in enumerate(boletim):
    print('{:<3} {:<9} {:<7}'.format(c, v[0], (v[1] + v[2]) / 2))
print('-=-' * 14)
while True:
    opc = int(input('Quer ver a nota de qual aluno (999 para parar): '))
    while opc > len(boletim) - 1 and opc != 999:
        print('Aluno não registrado!')
        opc = int(input('Quer ver a nota de qual aluno (999 para parar): '))
    if opc == 999:
        break
    print('As notas de {} são: {}'.format(boletim[opc][0], boletim[opc][1:]))