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
            return(f"Kon'nichiwa {nome}-san")
        case "espanhol" | '2':
            return(f"Hola {nome}")
        case "grego" | '3':
            return(f"Geia sou {nome}")
        case "francês" | '4':
            return(f"Salut {nome}")
        case "português" | '5':
            return(f"Olá, {nome}")
        case _:
            return(f"Hello {nome}")


meu_nome=input("Digite o seu nome: ").title()
idioma=input("Digite um idioma entre:\n1-Japonês\n2-Espanhol\n3-Grego\n4-Francês\n5-Português\n6-Inglês\n").lower()
print(saudacao_personalizada(meu_nome, idioma))
