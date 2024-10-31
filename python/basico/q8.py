#Escreva um programa que solicite ao usuário um número e verifique se ele é par ou ímpar. Imprima uma mensagem informando o resultado.

n=int(input("Digite um número: "))
if (n%2) != 0:
    print("{} é Impar".format(n))
else:
    print("{} é Par".format(n))