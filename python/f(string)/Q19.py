#Escreva um programa que solicite ao usuário para digitar uma frase e verifique se ela contém a palavra "Python"
f=input("Digite uma frase: ").split()
for i in range(len(f)):
    if f[i].lower() == "python":
        x="Tem Python"
        break
    else:
        x="Não Tem Python"
print(x)