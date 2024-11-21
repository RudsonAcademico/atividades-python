#Escreva um programa que solicite ao usuário para digitar uma frase e verifique se ela contém a palavra "Python"
f=input("Digite uma frase: ").lower()
p= "Tem Python" if f.count('python') >= 1 else "Não tem Python"
print(p)