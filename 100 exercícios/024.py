# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”

cid = str(input("Em qual cidade você nasceu? : ")).lower().split()
print('santo' in cid[0])