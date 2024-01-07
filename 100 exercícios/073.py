"""Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense."""

from time import sleep

times = ('Palmeiras', 'Grêmio', 'Atlético', 'Flamengo', 'Botafogo','Bragantino', 'Fluminense', 'Athletico-PR', 'Internacional', 'Fortaleza', 'São Paulo', 'Cuiabá', 'Corinthians', 'Cruzeiro', 'Vasco', 'Bahia', 'Santos', 'Goiás', 'Coritiba', 'América')

print('-- 5 Primeiros colocados são: ')
print('-=-' * 11)
for time in range(0, 5):
    print(f'    {time + 1} colocado -> {times[time]}')
    sleep(0.5)
print('-=-' * 11)
print('-- Os 4 últimos colocados são:')
for c in range(-4, 0, 1):
    print(f'{times.index(times[c]) + 1} - {times[c]}')
    sleep(0.5)
print('-=-' * 14)
print('-- Times em ordem alfabética:')
print('-=-' * 14)
sleep(0.5)
print(sorted(times))
print('-=-' * 14)
if 'Chapecoense' in times:
    print(f'A chapecoense está na posicão {times.index('Chapecoense')}')
else:
    print('A Chapecoense não está na lista.')
    sleep(0.5)
    print(f'Já o São Paulo está na posicão {times.index('São Paulo') + 1}')
print('-=-' * 14)
