#Escreva uma função chamada saudacao que aceita um nome como argumento e imprime "Olá, [nome]!".

def saudacao(nome:str) -> None:
    return f"Olá, {nome}!"


#Crie uma função dobro que aceita um número como argumento e retorna o dobro desse número.
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
