# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e IMAPARES e que se encontram no intervalo de 1 até 500.

print('Programa que mostra a soma entre os números múltiplos de 3')
intervalo = int(input('Informe o intervalo: '))
soma = 0
cont = 0
for c in range(1, intervalo + 1):
    if c % 3 == 0 and c % 2 != 0:
        soma += c
        cont += 1
print(f'A soma deu um total de {soma}')
print(f'Num total de {cont} valores')