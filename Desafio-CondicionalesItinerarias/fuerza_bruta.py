import getpass
from string import ascii_lowercase

#Ejercicio realizo en clases junto al profesor

password = getpass.getpass("Ingresa la password : \n").lower()


todas_letras = ascii_lowercase
contador = 0

for caracter in password :
    print(caracter)
    for letra in todas_letras :
        contador += 1
        if caracter == letra :
            break

print(f"El numero de intentos fue {contador}")