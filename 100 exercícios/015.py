#  Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

rodado = float(input("Quantos km's rodados: (km):"))
dia = int(input("Quantos dias: "))
valor_tot = (rodado * 0.15) + (dia * 60)
print(f"Valor dia: R${dia * 60:.2f}| valor km: R${rodado * 0.15:.2f}| valor total: R${valor_tot:.2f}")
