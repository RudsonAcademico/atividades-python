def fatorial(inicio):
    return inicio * fatorial(inicio-1) if inicio > 1 else inicio
    
def fibonacci(n):
    return 1 if n <= 2 else fibonacci(n-1) + fibonacci(n-2)
