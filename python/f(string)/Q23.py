#Escreva um programa que solicite ao usuário para digitar uma frase e verifique se todas as palavras estão em letras maiúsculas.

f = input("Digite uma frase: ")
n = "Esta tudo em maiusculo" if f == f.upper() else "Não esta tudo em maiusculo"
print(n)