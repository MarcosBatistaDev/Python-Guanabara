# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

num = int(input('Primeiro termo: '))
razao = int(input('Termo da PA: '))
cont = 0
opc = 10
while opc != -1:
    print(num, end='')
    cont += 1
    num += razao
    opc -= 1

    print(end=' -> ' if opc > 0 else ' -> Pausa')

    if opc == 0:
        opc = int(input('\nQuer mostrar mais quantos termos: '))
        if opc == 0:
            break

print(f'Ao todo foram {cont} termos mostrados!')
print('Fim do programa!')
