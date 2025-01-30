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
def saudacao_personalizada(nome:str, idioma="inglês" ) -> str:
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
    """
    Função que verifica se uma string fornecida como argumento representa um endereço de e-mail válido.
    Considere que um email válido não deve ter espaços, deve conter 01 arroba e terminar com .com
    """ 
    arroba = True if email.count("@") == 1 else False
    espaco = True if email.count(" ") == 0 else False
    final = True if email[-4:] == ".com" else False
    ponto = True if email.count("@.") == 0 else False
    if arroba and espaco and final and ponto:
        return True
    else:
        return False

"""
Escreva uma função calcular_pagamento que aceita os parâmetros nomeados horas_trabalhadas e taxa_hora e retorna o pagamento total.
"""
def calcular_pagamento(horas_trabalhadas:float, taxa_hora:float) -> float:
    """
    Função que aceita os parâmetros nomeados horas_trabalhadas e taxa_hora e retorna o pagamento total.
    """
    return horas_trabalhadas*taxa_hora

#Crie uma função que retorne o maior número dentre 3 elementos.

def maior_numero(a:int, b:int, c:int) -> int:
    #Função que retorne o maior número dentre 3 elementos.
    lista = sorted([a,b,c])
    return lista[-1]

#Escreva uma função em Python function que aceita uma string e retorna a quantidade de letras maiúsculas e minúsculas.
def contagem_letras(entrada):
    maiusculo = 0
    minusculo = 0
    for letra in entrada:
        if letra.isalpha():
            if letra.upper() == letra:
                maiusculo+=1
            elif letra.lower() == letra:
                minusculo+=1
    return maiusculo,minusculo

"""
Crie uma função chamada len_custom que aceita um iterável (por exemplo, uma lista ou uma string) como argumento e retorna o número de elementos no iterável.
Ela deve ter o mesmo comportamento que a função embutida len().
"""
def len_custom(entrada):
    saida = 0
    for i in entrada:
        saida+=1
    return saida

"""
Crie uma função chamada sum_custom que aceita uma lista de números como argumento e retorna a soma de todos os números na lista.
Ela deve ter o mesmo comportamento que a função embutida sum().
"""

def sum_custom(numeros):
    resultado=0
    for x in numeros:
        resultado+=x
    return resultado

"""
Crie uma função chamada max_custom que aceita uma lista de números como argumento e retorna o maior número na lista. 
Ela deve ter o mesmo comportamento que a função embutida max().
"""

def max_custom(lista):
    if lista:
        maior=lista[0]
        for i in lista:
            if i > maior:
                maior = i
    else:
        maior = None
    return maior

"""
Crie uma função chamada min_custom que aceita uma lista de números como argumento e retorna o menor número na lista.
Ela deve ter o mesmo comportamento que a função embutida min().
"""

def min_custom(lista):
    if lista:
        minimo=lista[0]
        for i in lista:
            if i < minimo:
                minimo = i
    else:
        minimo = None
    return minimo