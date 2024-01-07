# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = ('Manteiga', 21.39, 'Pão de forma', 9.12, 'Peito de peru', 5.65, 'Chedar', 6.34, 'Cuscuzeira', 65.77, 'Melancia', 12.33)

p = 0
v = 1
print('=-' * 19)
print('{:^38}'.format('Loja Barataumm'))
print('=-' * 19)
while True:
    print('  {:.<26}R$ {:>5}'.format(produtos[p], produtos[v]))
    p += 2
    v += 2
    if v == len(produtos) + 1:
        break
print('=-' * 19)