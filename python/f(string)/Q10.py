nome=input("Digite seu nome: ").split()
p=""
for i in range(len(nome)):
    p+=nome[i][0].upper()+"."
print(p)