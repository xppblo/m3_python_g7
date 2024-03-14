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
apellido = "Del LineAje DoRAdo"
print(apellido.title())
print(nombre + " " + apellido.title())

print(type(num)) #entrega el tipo de dato

print("KaKARotO".upper()) # entrega todo en mayusculas KAKAROTO
print("KaKARotO".lower()) # entrega todo el contenido en minusculas kakaroto

print(", ".join(["a","b","c"])) # une elementos separados


#Tipos de datos

entero = 1
decimal = 9.5
cadena = "esto es una cadena"
boleano = True

print(type(entero)) # int <class 'int'>
print(type(decimal)) # float <class 'float'>
print(type(cadena)) # str <class 'str'>
print(type(boleano)) # bolean <class 'bool'>

#presición de datos
promedio = (4+5+7)/3
print(f"el promedio es {promedio}")
print(f"resulta de la division {1/9:.4f}")
print(f"resulta de la division {round(1/9,3)}")
print(f"el promedio es {round(promedio,2)}")

#ingreso de datos

Nombre = input("Ingrese su nombre: \n")
print(f"Tu nombre es : {nombre}")
Edad = input("Ingrese su edad: \n")
print(f"Tu edad es : {Edad}")