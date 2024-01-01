"""Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso."""

from time import sleep

print('-=-' * 10)
num_1 = int(input('Digite um número: '))
num_2 = int(input('Outro número: '))
print('-=-' * 10)

while True:
    opc = int(input("""[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
Sua escolha: """))
    print('-=-' * 10)
    
    # Somando
    if opc == 1:
        print(f'{num_1} + {num_2} = {num_1 + num_2}')
        print('-=-' * 10)

    # Multiplicando
    elif opc == 2:
        print(f'{num_1} x {num_2} = {num_1 * num_2}')
        print('-=-' * 10)

    # Maior
    elif opc == 3:
        if num_1 > num_2:
            print(f'{num_1} é maior que {num_2}.')
        elif num_2 > num_1:
            print(f'{num_2} é maior que {num_1}.')
        else:
            print(f'{num_1} é igual a {num_2}')
        print('-=-' * 10)

    # Novos números
    elif opc == 4:
        print('Escolha novos números')
        print('-=-' * 10)
        num_1 = int(input('Digite um número: '))
        num_2 = int(input('Outro número: '))
        print('-=-' * 10)


    # Saindo do programa
    elif opc == 5:
        break

    # Escolha inválida
    else:
        print('Opcao inválida')
        print('Encerrando programa!')
        sleep(2)
        print('-=-' * 10)
        break

print('      Fim do programa.')
print('-=-' * 10)
