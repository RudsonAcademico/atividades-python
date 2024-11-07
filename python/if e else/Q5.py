#Classificação de Idade: Peça a idade do usuário e classifique-a em "Criança" (0-12), "Adolescente" (13-19), "Adulto" (20-59) ou "Idoso" (60+).
idade=int(input("Digite a sua idade: "))

if idade >= 0 and idade < 13:
    print("Você é uma criança")
elif idade >= 13 and idade < 20:
    print("Você é um adolecente")
elif idade >= 20 and idade < 60:
    print("Você é um adulto")
elif idade >= 60:
    print("Você é um idoso")
else:
    print("idade invalida")