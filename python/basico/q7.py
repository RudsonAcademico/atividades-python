#Escreva um programa que solicite ao usuário o seu salário mensal e o número de meses trabalhados no ano. Calcule e imprima o salário anual.

s=float(input("Digite seu salário: "))
m=int(input("Digite quantos meses você trabalha no ano: "))

print("Seu Salário anual é de {}".format(s*m))