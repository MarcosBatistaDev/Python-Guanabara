# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

lista_alunos = [str(input("Primeiro aluno: ")), str(input("Segundo aluno: ")), str(input("Terceiro aluno: ")), str(input("Quarto aluno: ")), str(input("Quinto aluno: "))]
print(f"Ordem atual: {lista_alunos}")
print("A nova ordem será:")
shuffle(lista_alunos)
print(f"{lista_alunos}")