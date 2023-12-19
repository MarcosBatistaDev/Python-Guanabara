# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice

lista_alunos = [str(input("Primeiro aluno: ")), str(input("Segundo aluno: ")), str(input("Terceiro aluno: ")), str(input("Quarto aluno: ")), str(input("Quinto aluno: "))]
print(f"O aluno escolhido foi {choice(lista_alunos)}")
