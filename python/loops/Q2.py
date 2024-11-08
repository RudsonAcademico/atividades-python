#Escreva um programa que peça ao usuário para digitar um número e, em seguida, imprima a tabuada desse número (de 1 a 10) utilizando um loop "for".
n=int(input("Digite um numero: "))
for i in range(11):
    print(f"{n} x {i} = {n*i}")