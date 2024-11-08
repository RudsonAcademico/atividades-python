#Escreva um programa que peça ao usuário para digitar uma frase e, em seguida, conte quantas vogais (a, e, i, o, u) existem na frase utilizando um loop "for".
p=input("Digite uma frase: ").lower()
v=["a", "e", "i", "o", "u"]
n=0
for i in range(len(p)):
    for x in range(len(v)):
        if p[i] == v[x]:
            n+=1
print(f"Tem {n} vogais nessa frase")