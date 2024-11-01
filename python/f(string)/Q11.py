#Escreva um programa que solicite ao usuário uma quantidade de horas, minutos e segundos, e imprima uma mensagem formatada mostrando o total de segundos. Por exemplo: "O total de segundos é {total_segundos}."
h=input("Digite as horas com minutos e segundos.\nExemplo(23:59:59)\n").split(":")
s=0
m=3600
for i in range(len(h)):
    s+=int(h[i])*m
    m/=60
print(f"O total de segundos é {s:.0f}")