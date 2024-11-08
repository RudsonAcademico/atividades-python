#Escreva um programa que peça ao usuário para digitar uma série de números (um por linha) e pare quando o usuário digitar um número negativo. Em seguida, calcule e imprima a média dos números digitados.

n=int(input("Digite um numero para calcular a media(e qualquer numero negativo para finalizar):"))
c=1
m=n
while n >= 0:
    print(c, m)
    n=int(input("Digite um numero para calcular a media(e qualquer numero negativo para finalizar):"))
    if n >=0:
        m+=n
        c+=1
if m < 0:
    print("Número negativo")
else:
    print(f"A media de todos os numeros é: {m/c}")