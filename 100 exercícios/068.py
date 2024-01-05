# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.


from random import randint

c = 0
print('-=-' * 14)
print('           Jogo Ímpar ou Par !!')
print('-=-' * 14)
while True:
    num = int(input('Digite um número: '))
    opc = str(input('Par ou ímpar? [P/I]: ')).strip().lower()
    while opc != 'p' and opc != 'i':
        opc = str(input('Par ou ímpar? [P/I]: ')).strip().lower()

    computador = randint(1, 10)
    soma = num + computador

    print(f'Você jogou {num} e o computador jogou {computador}. Deu {soma}', end=' ')
    if soma % 2 == 0:
        print('[  Par  ]')
    else:
        print('[  Ímpar  ]')
    
    print('-=-' * 14)
    if (opc == 'p' and soma % 2 == 0) or opc == 'i' and soma % 2 != 0:
        print('           Você VENCEU!!')
        print('-=-' * 14)
        c += 1
    else:
        print('           Você PERDEU!!')
        break
print('-=-' * 14)
print(f'           Você venceu {c} vezes.')
print('-=-' * 14)

    
