"""
Escreva um programa que peça ao usuário para adivinhar um número secreto entre 1 e 100. 
O programa deve informar se o palpite é muito alto, muito baixo ou correto. 
Continue pedindo ao usuário para adivinhar até que ele acerte o número utilizando um loop "while".
"""
import random
n=random.randrange(0, 100)
p=int(input("Tente adivinhar um numero: "))
while p != n:
    if p > n:
        print("Menos")
    elif p < n:
        print("Mais")
    p=int(input("Tente adivinhar um numero: "))
print("Correto!")