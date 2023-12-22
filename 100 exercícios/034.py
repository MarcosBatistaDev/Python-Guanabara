# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite seu salário: R$'))
if salario <= 1250:
    salario = salario + (salario * 0.15)
    print('Você recebeu um aumento de 15%')
else:
    salario = salario + (salario * 0.1)
    print('Você recebeu um aumento de 10%')
print(f'Seu novo salário será de R${salario:.2f}')