#Escreva um programa que peça ao usuário para digitar uma senha e continue pedindo até que o usuário digite a senha correta. Quando a senha estiver correta, imprima uma mensagem de boas-vindas.
s="paosemh"
p=input("Digite a senha:")
while p != s:
    p=input("Erro!\nDigite a senha correta:")
print("Bem vindo")