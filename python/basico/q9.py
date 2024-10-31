#Escreva um programa que solicite ao usuário dois valores booleanos (True ou False) e armazene-os em variáveis. 
#Em seguida, aplique os operadores lógicos "and", "or" e "not" entre essas variáveis e imprima os resultados.
q=bool(int(input("Escolha um valor Booleano\nPara False Digite 0\nPara True Digite 1\n")))
p=bool(int(input("Escolha um valor Booleano\nPara False Digite 0\nPara True Digite 1\n")))

print(f"Operador de Conjunção Q and P: {q and p}")
print(f"Operador de Disjunção Q or P: {q or p}")
print(f"Operador de Negação Q: {not q}")
print(f"Operador de Negação P: {not p}")