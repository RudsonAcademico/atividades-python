"""
Verificação de Triângulo:
Peça ao usuário o comprimento de três lados e verifique se eles podem formar um triângulo.
Se sim, determine se é um triângulo equilátero, isósceles ou escaleno.
"""

l1=float(input("Digite o tomanho do lado 1: "))
l2=float(input("Digite o tomanho do lado 2: "))
l3=float(input("Digite o tomanho do lado 3: "))
if (l1 >= l2 + l3) or (l2 >= l1 + l3) or (l3 >= l2 + l1):
    print("Não é um triangulo valido")
else:
    if l1 == l2 and l2 == l3:
        print("O triangulo é Equilátero")
    elif (l1 == l2) or (l2 == l3) or (l3 == l1):
        print("O triangulo é Isósceles")
    else:
        print("O triangulo é escaleno")