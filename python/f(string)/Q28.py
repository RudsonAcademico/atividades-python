#Escreva um programa que solicite ao usuário para digitar uma frase e, em seguida, divida a frase em palavras individuais e as imprima em linhas separadas.

f=input("Digite uma frase: ").split()
for x in range(len(f)):
    print(f[x])