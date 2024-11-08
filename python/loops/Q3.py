#Escreva um programa que peça ao usuário para digitar uma palavra e, em seguida, imprima cada letra da palavra em uma linha separada utilizando um loop "for".
p=input("Digite uma palavra: ")
for i in range(len(p)):
    print(p[i])