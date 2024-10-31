#Escreva um programa que solicite ao usuário dois números inteiros e armazene-os em variáveis.
#Em seguida, calcule e imprima a soma, subtração, multiplicação e divisão desses números.

n1=int(input("Digite um Número: "))
n2=int(input("Digite um outro Número: "))

print("{}+{}={}".format(n1,n2,(n1+n2)))
print("{}-{}={}".format(n1,n2,(n1-n2)))
print("{}x{}={}".format(n1,n2,(n1*n2)))
print("{}/{}={}".format(n1,n2,(n1/n2)))
