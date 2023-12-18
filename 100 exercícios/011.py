#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

larg = float(input("Largura da parede (m):"))
alt = float(input("Altura da parede (m):"))
area = larg * alt
print(f"Para pintar uma parede de {larg:.2f}x{alt:.2f} e area de {area:.2f}m² será necessário usar {area/2:.2f}L de tinta.")