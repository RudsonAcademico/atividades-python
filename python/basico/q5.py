#Escreva um programa que solicite ao usuário o raio de um círculo e calcule a área e o perímetro desse círculo. Imprima os resultados formatados.
import math
r=float(input("Digite o valor do raio: "))
a=math.pi*(r**2)
p=r*(2*math.pi)

print("A área do circulo é {:.2f} e o seu perímetro é {:.2f}".format(a,p))