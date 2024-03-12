#comentario de una linea
"""
comentario multilinea
mas de
una linea
"""
print("Estamos en nuestro primer ejercicio de python")
print(2 + 2)
print(12 - 2)
print(2 * 2)
#print(2 / 0) -> Error no se puede dividir por 0
print(100 / 99) #-> el resultado siempre sera un numero float

num = 23
print(num)

# LIMITANTES
# No esta permitido la suma de letras y numeros
#print("texto"+12) Error no se pueden concatener numero y letras

# INTERPOLACION
print(f"el numero es {num}")

nombre = "Miquella"

print(f"Tu nombre es {nombre} \n y tu edad es {num}")
print("Tu nombre es "+nombre)

# string.format
print("Tu nombre es {} y tu edad es {}".format(nombre,num))

# formato con %: %s para string %d para numeros
print("Tu nombre es %s y tu eddad es %d" % (nombre, num))

# Metodo con cadena
apellido = "Del Lineaje Dorado"
print(apellido.title())
