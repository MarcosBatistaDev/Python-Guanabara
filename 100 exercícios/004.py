# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

valor = str(input("Digite algo: "))
print("Tipo primitivo:", type(valor))
print("São só espacos:",valor.isspace())
print("São números:", valor.isnumeric())
print("São letras:", valor.isalpha())
print("São letras e/ou números:", valor.isalnum())
print("São letras maiúsculas:", valor.isupper())
print("São letras minúsculas:", valor.islower())
print("Está capitalizado:", valor.istitle())
