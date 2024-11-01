#Escreva um programa que solicite ao usuário seu nome completo e imprima as iniciais de cada palavra em letras maiúsculas. Por exemplo, se o nome for "Fulano de Tal", o programa deve imprimir "F.D.T."
nome=input("Digite seu nome: ").split()
p=""
for i in range(len(nome)):
    p+=nome[i][0].upper()+"."
print(p)