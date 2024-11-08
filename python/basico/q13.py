#Escreva um programa em Python que solicite ao usuário dois números inteiros e troque os valores das variáveis. Em seguida, imprima os valores atualizados.
n1=int(input("Digite um numero: "))
n2=int(input("Digite outro numero: "))
print(f"Antes da troca: {n1=}, {n2=}")
n3=n1
n1=n2
n2=n3
print(f"Depois da troca: {n1=}, {n2=}")