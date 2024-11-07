"""
Validação de Login: Crie um programa que pede ao usuário um nome de usuário e uma senha.
Se o nome de usuário for "admin" e a senha for "12345", exiba "Acesso concedido", caso contrário,
exiba "Acesso negado".
"""
login=input("Digite seu usuário: ")
if login == "admin":
    senha=input("Digite a senha: ")
    if senha == "12345":
        print("Acesso Concedido")
    else:
        print("Acesso Negado") 
else:
    print("Acesso Negado")