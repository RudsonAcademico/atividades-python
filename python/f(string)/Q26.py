#Escreva um programa que peça ao usuário para digitar uma frase e imprima o número de caracteres na frase.
f=input("Digite uma frase: ")
print(f"'{f}' tem {len(f.replace(" ", ""))} caracteres")