#Escreva um programa que solicite ao usuário para digitar seu endereço de e-mail e extraia o nome de usuário (parte antes do "@") e o domínio (parte depois do "@").
email=input("Digite seu email: ").split("@")
print(f"nome de usuario {email[0]}\ndominio {email[1]}")
