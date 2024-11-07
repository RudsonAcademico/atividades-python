"""
Validação de Login: Crie um programa que pede ao usuário um nome de usuário e uma senha.
Se o nome de usuário for "admin" e a senha for "12345", exiba "Acesso concedido", caso contrário,
exiba "Acesso negado".
"""
t=4
login=input("Digite seu usuário: ")
while login != "admin":
    print("Usuario Invalido")
    login=input("Digite seu usuário: ")
    if t == 0:
        print("Tentativas exedidas")
        break
    t=t-1
t=4
if login == "admin":
    senha=input("Digite a senha: ")
    while senha != "12345":
        print("Usuario Invalido")
        senha=input("Digite seu usuário: ")
        if t == 0:
            print("Tentativas exedidas")
            break
        t=t-1
    
else:
    print("Acesso negado")