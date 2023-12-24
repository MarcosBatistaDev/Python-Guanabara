# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano_nasc = int(input('Ano de nascimento: '))
idade = date.today().year - ano_nasc

print(f'Quem nasceu em {ano_nasc} tem {idade} anos de idade no ano de {date.today().year}.')

if idade < 18:
    print(f'Ainda faltam {18 - idade} anos para seu alistamento (seu alistamento será em {(18 - idade) + date.today().year}.)')
elif idade == 18:
    print('Você deve se alistar imediatamente!')
else:
    print(f'Você ja deveria ter se alistado há {idade - 18} anos.')
    print(f'Seu alistamento foi no ano de {date.today().year - (idade - 18)}.')