# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

from time import sleep

jogadores = list()
jogador = dict()
gols = list()
while True:
    jogador['nome'] = str(input('Nome do jogador: ').strip().title())
    num_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
    for c in range(0, num_partidas):
        gols.append(int(input(f'Quantos gols na partida {c + 1}: ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    resp = str(input('Quer continuar (S/N): ')).strip().lower()
    while resp != 's' and resp != 'n':
        print('=> Responda apenas com S ou N.')
        resp = str(input('Quer continuar (S/N): ')).strip().lower()
    jogadores.append(jogador.copy())
    jogador.clear()
    gols.clear()   
    if resp == 'n':
        break
print('-=-' * 15)
print('{:<4} {:<14} {:<20} {}'.format('cod', 'nome', 'gols', 'total'))
for c, v in enumerate(jogadores):
    print('{:<4} {:<14} {:<20} {}'.format(c, str(v['nome']), str(v['gols']), str(v['total'])))
print('-=-' * 15)
print('Consultar saldo de Gols')
while True:
    print('-=-' * 15)
    resp = int(input('Quer consultar qual jogador (999 para parar): '))
    if resp == 999:
        break
    while resp > len(jogadores) - 1:
        print(f'Não existe jogador com código {resp}.')
        resp = int(input('Quer consultar qual jogador (999 para parar): '))
    print(f'---  LEVANTAMENTO DO JOGADOR {jogadores[resp]['nome']}  ---')
    for c, v in enumerate(jogadores[resp]['gols']):
        print(f'Na partida {c + 1} fez {v} gol(s).')
        sleep(0.7)
    

