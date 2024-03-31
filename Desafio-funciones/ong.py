def factorial(n):    
    if n < 0:
        return print("No se puede calcular el factorial de numeros negativos")
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
    
def productoria(lista):
    resultado = 1
    for num in lista:
        resultado *= num
    return resultado
    