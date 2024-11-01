#Escreva um programa que solicite ao usuário dois números e imprima uma mensagem formatada mostrando a soma, subtração, multiplicação e divisão dos números. Por exemplo: "A soma de {num1} e {num2} é {soma}."
num1=int(input("Digite o primeiro Número:"))
num2=int(input("Digite o segundo Número:"))
print(f"A soma de {num1} e {num2} é {num1+num2}.\nA subtração de {num1} e {num2} é {num1-num2}.\nA multiplicação de {num1} e {num2} é {num1*num2}.\nA divisão de {num1} e {num2} é {num1/num2}.")
