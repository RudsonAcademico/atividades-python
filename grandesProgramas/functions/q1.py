#Escreva uma função chamada saudacao que aceita um nome como argumento e imprime "Olá, [nome]!".

def saudacao(nome:str) -> None:
    return f"Olá, {nome}!"


#Crie uma função dobro que aceita um número como argumento e retorna o dobro desse número
def dobro(numero:int) -> int:
    numero*=2
    return numero


"""
Crie uma função chamada saudacao_personalizada que aceita um nome e um idioma como argumentos.
O idioma é opcional e padrão para "inglês". A função deve retornar uma saudação no idioma especificado.
"""
def saudacao_personalizada(nome:str, idioma:str) -> str:
    """
    Uma função que aceita um nome e um idioma como argumentos.
    O idioma é opcional e padrão para "inglês". A função deve retornar uma saudação no idioma especificado.
    """
    match idioma:
        case "japonês" | '1':
            return(f"Kon'nichiwa {nome}-san!")
        case "espanhol" | '2':
            return(f"Hola, {nome}!")
        case "grego" | '3':
            return(f"Geia sou {nome}!")
        case "francês" | '4':
            return(f"Bonjour, {nome}!")
        case "português" | '5':
            return(f"Olá, {nome}!")
        case _:
            return(f"Hello, {nome}!")

#Escreva uma função potencia que aceita uma base e um expoente (com expoente padrão igual a 2) e retorna a base elevada ao expoente
def potencia(base:int, expoente:int) -> int:
    #Uma função potencia que aceita uma base e um expoente (com expoente padrão igual a 2) e retorna a base elevada ao expoente
    if expoente == None:
        return(base**2)
    else:
        return(base**expoente)

"""
Crie uma função chamada idade_valida que verifica se a idade fornecida como argumento é um número inteiro válido entre 0 e 150
"""
def idade_valida(idade:int) -> bool:
    if type(idade) == int:
        if idade >= 0 and idade <= 150:
            return True
        else: 
            return False
    else:
        return False

"""
Implemente uma função validar_email que verifica se uma string fornecida como argumento representa um endereço de e-mail válido.
Considere que um email válido não deve ter espaços, deve conter 01 arroba e terminar com .com
"""
def validar_email(email:str) -> bool:
    arroba = True if email.count("@") == 1 else False
    espaco = True if email.count(" ") != 0 else False
    final = True if email[-4:] == ".com" else False
    ponto = True if email.count("@.") != 0 else False
    if arroba and espaco and final and ponto:
        return True
    else:
        return False