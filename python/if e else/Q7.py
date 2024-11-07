#Conversão de Notas: Escreva um programa que converte uma nota de 0 a 100 em uma escala de conceitos: A (90-100), B (80-89), C (70-79), D (60-69) e F (0-59).
n=int(input("Digite uma nota entre 0 e 100: "))

if n >= 90 and n <= 100:
    print("Essa é uma nota A")
elif n < 90 and n >= 80:
    print("Essa é uma nota B")
elif n < 80 and n >= 70:
    print("Essa é uma nota C")
elif n < 70 and n >= 60:
    print("Essa é uma nota D")
elif n < 60:
    print("Essa é uma nota F")