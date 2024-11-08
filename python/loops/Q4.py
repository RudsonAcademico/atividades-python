#Escreva um programa que utilize um loop "for" para calcular a soma de todos os números ímpares de 1 a 100.
n=0
for x in range(101):
    if x%2 != 0:
        n+=x
print(n)