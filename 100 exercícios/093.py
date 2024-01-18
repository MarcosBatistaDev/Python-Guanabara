# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador_dados = dict()
jogador_dados['nome'] = str(input('Nome: ')).strip().title()
num_partidas = int(input(f'Quantas partidas o {jogador_dados["nome"]} jogou: '))
gols = list()
for c in range(0, num_partidas):
    gols.append(int(input(f'Quantos gols na {c+1}ª partida: ')))
jogador_dados['gols'] = gols
jogador_dados['total'] = sum(gols)
print('-=-' * 14)
print(jogador_dados)
print('-=-' * 14)
for k, v in jogador_dados.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=-' * 14)
print(f'O jogador {jogador_dados["nome"]} jogou {num_partidas} partidas.')
for c, v in enumerate(gols):
    print(f'  => Na partida {c}, fez {v} gols.')
print(f'Foi um total de {jogador_dados["total"]} gols.')