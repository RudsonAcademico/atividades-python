#Escreva um programa para ler uma frase, imprima esta frase com as palavras ordenadas em ordem crescente de comprimento das strings.
f=input("Digite uma frase: ")
f_ordem= sorted(f.split(), key=len)
print(f"'{f}' ordenado da menor pra o maior {f_ordem}")