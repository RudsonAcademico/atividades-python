"""
Escreva um programa que peça ao usuário para adivinhar um número secreto entre 1 e 100. 
O programa deve informar se o palpite é muito alto, muito baixo ou correto. 
Continue pedindo ao usuário para adivinhar até que ele acerte o número utilizando um loop "while".
"""
from random import randint
n=randint(0, 100)
p=int(input("Tente adivinhar o numero: "))
t=1
while p != n:
    if p > n:
        print("Menos")
    elif p < n:
        print("Mais")
    else:
        print(f"Você Ganhou! com {t} tentativas")
    p=int(input("Tente adivinhar o numero: "))
    t+=1
    if t >= 5:
        p=n
        print("Você Perdeu!")
