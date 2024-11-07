#Maior de Três Números: Escreva um programa que solicita três números ao usuário e retorna o maior dentre eles.
n1 = int(input("digite um numero: "))
n2 = int(input("digite outro numero: "))
n3 = int(input("digite um outro numero: "))

if n1 > n2:
    if n1 > n3:
        print(f"{n1} é o maior")
    else:
        print(f"{n3} é o maior")
else:
    if n2 > n3:
        print(f"{n2} é o maior")
    else:
        print(f"{n3} é o maior")