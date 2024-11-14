"""
Escreva um programa que peça ao usuário para adivinhar um número secreto entre 1 e 100. 
O programa deve informar se o palpite é muito alto, muito baixo ou correto. 
Continue pedindo ao usuário para adivinhar até que ele acerte o número utilizando um loop "while".
"""
from random import randint
d = input("Escolha uma dificuldade:\nF:Facil\nM:Médio\nD:Dificil\n").lower()
match d:
    case 'f':
        MIN, MAX = 0, 10
        MT= 5
        d="Facil"
    case 'm':
        MIN, MAX = 0, 100
        MT= 5
        d="Medio"
    case 'd':
        d="Dificil"
        MIN, MAX = 0, 1000
        MT= 5
    case _:
        d="Impossivel"
        MIN, MAX = 0, 100000
        MT= 2
n=randint(MIN, MAX)
print(f'Você tem {MT} tentativas')
p=int(input(f"Tente adivinhar o numero entre {MIN} e {MAX}: "))

t=1
while p != n:
    if p > n:
        print(f"Menos. Você tem {MT-t} tentativas")
    elif p < n:
        print(f"Mais. Você tem {MT-t} tentativas")
    else:
        print(f"Você Ganhou! com {t} tentativas")
    p=int(input("Tente adivinhar o numero: "))
    t+=1
    if t >= MT:
        p=n
        print(f"Você Perdeu! A resposta era {p}")
