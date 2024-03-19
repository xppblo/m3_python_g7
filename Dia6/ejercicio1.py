"""
CONDICION IF

si se cumple la condicion, entonces se ejecuta el codigo

if condicion:
    #codigo a ejecutar si es verdadero

"""

edad = int(input("Ingrese su edad :\n"))

if edad > 18:
    print("Eres mayor de edad")
elif edad == 18:
    print("Tienes 18 años")
else:
    print("Eres menor de edad")

print("Fin del progarma")

if edad == 0:
    print("La edad es 0")
elif edad % 2 == 0:
    print("La edad es par")
else:
    print("La edad es impar")
    
#Crear un ingreso de password
#Revisar si la contraseña tiene minimo 6 caracteres

passwarod = input("Ingrese su contraseña :\n")

if len(passwarod)<6:
    print("La password es demasiado corto")