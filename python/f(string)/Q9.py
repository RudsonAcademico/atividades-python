#Escreva um programa que solicite ao usuário uma frase e substitua todas as vogais por asteriscos (*). Em seguida, imprima a frase formatada.
p=input("Digite uma frase: ")
vog=["a","e","i","o","u","A","E","I","O","U"]
for x in range(len(vog)):
    p=(p.replace(vog[x],"*"))
print(p)