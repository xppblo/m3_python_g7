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

def calcular(**elementos):
    for clave,valor in elementos.items():
        if "fact" in clave:
            print(f"El factorial de {valor} es {factorial(valor)}")
        elif "prod" in clave:
            print(f"La productoria de {valor} es {productoria(valor)}")
            
calcular(fact_1 = 5, prod_1=[4,6,7,4,3], fact_2=6)