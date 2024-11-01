#Escreva um programa que solicite ao usuário para digitar uma frase e verifique se ela termina com um ponto final.
f=input("Digite uma frase: ")
p="A frase tem ponto final" if f[-1] == "." else "A frase não tem ponto final"
print(f"{f} {p}")