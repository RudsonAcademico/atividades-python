#Calculadora Simples: Faça uma calculadora que pede ao usuário dois números e uma operação (+, -, *, /) e retorna o resultado dessa operação.
n1= int(input("Digite um numero: "))
n2= int(input("Digite outro numero: "))
op=input("Digite a operação (+, -, *, /): ")
if op == "+":
    print(n1+n2)
elif op == "-":
    print(n1-n2)
elif op == "*":
    print(n1*n2)
elif op == "/":
    print(n1/n2)
else:
    print("Operação Invalida")