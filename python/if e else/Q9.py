"""
Calculadora de IMC: Peça ao usuário seu peso e altura e calcule o índice de massa corporal (IMC).
Em seguida, mostre uma mensagem indicando se a pessoa está abaixo do peso, com peso normal,
com sobrepeso, obesa ou muito obesa.
"""
peso=float(input("Indique sua peso em quilos: "))
altura=float(input("Indique a altura em metros: "))
imc= peso/(altura**2)
if imc <= 18.5:
    print("Sua classificação é abaixo do peso")
elif imc >= 18.6 and imc < 25:
    print("Sua classificação é normal")
elif imc >= 25 and imc < 30:
    print("Sua classificação é sobrepeso")
elif imc >= 30 and imc < 35:
    print("Sua classificação é obeso")
elif imc >= 35 and imc < 40:
    print("Sua classificação é muito obeso")
else:
    print("Fora da classificação procure um medico")