p=input("Digite uma palavra: ").lower()
if p == p[::-1]:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")