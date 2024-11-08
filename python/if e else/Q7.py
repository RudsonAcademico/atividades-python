#Conversão de Notas: Escreva um programa que converte uma nota de 0 a 100 em uma escala de conceitos: A (90-100), B (80-89), C (70-79), D (60-69) e F (0-59).
n=int(input("Digite uma nota entre 0 e 100: "))

if n in list(range(90,101)):
    print("Essa é uma nota A")
elif n in list(range(80,90)):
    print("Essa é uma nota B")
elif n in list(range(70,80)):
    print("Essa é uma nota C")
elif n in list(range(60,70)):
    print("Essa é uma nota D")
elif n in list(range(0,60)):
    print("Essa é uma nota F")