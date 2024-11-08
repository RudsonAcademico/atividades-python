#Verificação de Ano Bissexto: Escreva um programa que verifica se um ano fornecido pelo usuário é bissexto ou não.
ano=int(input("Digite um ano: "))
if ano%4==0:
    if ano%100==0:
        if ano%400==0:
            print("é bissexto")
        else:
            print("não é bissexto")
    else:
        print("é bissexto")
else:
    print("não é bissexto")

if (ano%400==0) or ((ano%4==0) and (ano%100!=0)):
    print("Bissexto")
else:
    print("Não bissexto")