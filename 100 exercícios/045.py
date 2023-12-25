# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint

print('===== GAME JO KEN PO =====')
opc = int(input("""[1] Pedra
[2] Papel
[3] Tesoura
Sua escolha: """))
bot_choice = randint(1, 3)
list_moves = ['Pedra', 'Papel', 'Tesoura']

if opc not in (1, 2, 3):
    print('Escolha inválida!')
else:
    print('-=-' * 12)
    print(f'Você esolheu {list_moves[opc - 1]}')
    print(f'O computador escolheu {list_moves[bot_choice - 1]}')
    print('-=-' * 12)
    if opc == 1:
        if opc == bot_choice:
            print('Empate!')
        elif bot_choice == 2:
            print('O computador venceu!')
        else:
            print('Parabéns você Venceu!')

    elif opc == 2:
        if opc == bot_choice:
            print('Empate!')
        elif bot_choice == 1:
            print('Parabéns você Venceu!')      
        else:
            print('O computador venceu!')

    elif opc == 3:
        if opc == bot_choice:
            print('Empate!')
        elif bot_choice == 2:
            print('Parabéns você Venceu!')
        else:
            print('O computador venceu!')

    else:
        print('Escolha inválida!')
print('-=-' * 12)
