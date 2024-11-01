#Escreva um programa que verifique se uma palavra é um palíndromo (lê-se igual de trás para frente). Exemplo: "radar"
p=input("Digite uma palavra: ").lower()
if p == p[::-1]:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")