"""
Ciclo_for
for variable in iterable:

"""
# El valor que se agrega dentro no es considerado
# En este caso es del 0 al 9
for i in range(10) :
    print(i)
    
print("")

# Comienza a imprimir desde el 4 hasta el 9 y se va incrementando de 1 en 1
for i in range(4,10,2) :
    print(i)

#Simil en javascript del for anterior
"""
for (let i = 4; i < 10; i++) {
    console.log(i);
}
"""

#Listas
numeros =[2,"4",True,3,"5"]

for numeros in numeros :
    print(numeros)
    
print("")
#String -> son similares a las listas
texto = "Hola Mundo"
for caracter in texto :
    print(caracter)

print("")
#Diccionario
datos_personales = {
    "Nombre" : "Pablo",
    "Apellido" : "Hernández",
    "Edad" : 26
}

for clave in datos_personales :
    print(clave) #Imprime las claves
    
print("")

for clave in datos_personales :
    print(datos_personales[clave]) # Imprime los valores de las claves
    
print("")

for clave,valor in datos_personales.items() :
    print(f"clave : {clave} - valor : {valor}")

print("")
    
for clave in datos_personales.keys():
    print(clave) # Forma de acceder a la clave

print("")

for valor in datos_personales.values():
    print(valor) # Forma de acceder a los valores

print("")
#ENUMERATE

for posicion,caracter in enumerate(texto) :
    print(f"La posición {posicion} del caracter {caracter}")

print("")


for posicion,numero in enumerate(numeros) :
    print(f"La posición {posicion} del numero {numero}")

print("")

prefijo = ['La','El','La','El']
frutas = ['manzana', 'platano','frutilla','tomate']
colores = ['verde','amarillo','roja','rojo']
for p, fruta, color in zip(prefijo, frutas, colores):
    print(f'{p} {fruta} es de color {color}')
    
print("")

numeros=[2,"4",True,3,"5",[2,5,8],{"clave":"valor"}]
for numero in numeros:
    print(numero)
    if numero == 3:
        break
print("Fuera del for")