# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint

jogos = list()
jogo = list()

print('-' * 30)
num_jogos = int(input('   Quantos jogos: '))
print('-' * 30)

while True:
    if len(jogos) == num_jogos:
        break
    for c in range(0, 6):
        num_sorteado = randint(1, 60)
        while num_sorteado in jogo:
            num_sorteado = randint(1, 60)
        jogo.append(num_sorteado)
    jogos.append(jogo[:])
    jogo.clear()
print(f'-=-=-= Sorteado {num_jogos} Jogos -=-=-=')
for pos, jogo_feito in enumerate(jogos):
    print(f'Jogo {pos + 1}: {sorted(jogo_feito)}')