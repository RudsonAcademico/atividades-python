#Escreva um programa que peça ao usuário para digitar uma palavra e, em seguida, imprima a palavra ao contrário utilizando um loop "for".
p=input("Digite uma palavra: ")
q=""
for i in range(len(p)-1, -1, -1):
    q+=p[i]
print(q)