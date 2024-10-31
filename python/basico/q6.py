#Escreva um programa que solicite ao usuário uma temperatura em graus Celsius e converta-a para Fahrenheit. Imprima o resultado formatado.
c= float(input("Digite a temperatura em Celsius: "))
f= (c*9/5)+32

print("Se esta {}°C então esta {:.1f}°F".format(c, f))
