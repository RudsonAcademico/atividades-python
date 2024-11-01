#Escreva um programa que solicite ao usuário uma frase e imprima uma mensagem formatada mostrando a quantidade de caracteres, palavras e linhas na frase.
f=input("Digite uma frase: ")
print(f"{f} tem {len(f)} caracteres e {len(f.split())} linhas")