#  Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input("Nome completo: ")).strip().lower()
print("Seu nome tem Silva?", 'silva' in nome)