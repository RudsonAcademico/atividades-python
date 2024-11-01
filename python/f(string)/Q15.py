#Escreva um programa que solicite ao usuário um nome e um número inteiro e imprima uma mensagem formatada repetindo o nome o número de vezes especificado. Por exemplo, se o nome for "João" e o número for 3, o programa deve imprimir "JoãoJoãoJoão".
f=input("Digite seu nome:")
i=int(input("Digite um número:"))
for x in range(i-2):
    f+=f
print(f)