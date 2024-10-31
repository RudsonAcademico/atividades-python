nome=input("Digite seu nome: ")
p=nome.split()
nome=""
for i in range(len(p)):
    nome+=p[i][0].upper()+"."
print(nome)