#  Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

prec_produto = float(input("Preço do produto R$"))
prec_desconto = prec_produto - (prec_produto / 100 * 5)
print(f"O produto que custava R${prec_produto:.2f}, com 5% de desconto custará R${prec_desconto:.2f}")