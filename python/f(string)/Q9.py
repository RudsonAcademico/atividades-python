p=input("Digite uma frase: ")
vog=["a","e","i","o","u","A","E","I","O","U"]
for x in range(len(vog)):
    p=(p.replace(vog[x],"*"))
print(p)