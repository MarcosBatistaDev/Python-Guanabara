#Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável. 

def escreva(msg):
    print('-' * (len(msg) + 2))
    print('', msg)
    print('-' * (len(msg) + 2))

while True:
    mensagem = str(input('Digite uma palavra qualquer: '))
    if mensagem == 'pare':
        break
    escreva(mensagem)