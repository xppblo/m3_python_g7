"""
    while condicion:
        #codigo a ejecutar
    
    import getpass

    password = getpass.getpass("Ingrese su contraseña:\n")

    while len(password) <6 :
        password = getpass.getpass("Su contraseña es muy corta, ingresar un numero de caracteres mayor a 6")

    while password != "Hola Mundo" :
        password = getpass.getpass("No adivinaste la contraseña, Ingrese su contraseña nuevamente:\n")
    
"""

i = 0
while i < 10 :
    print(f"El valor de i es : {i}")
    i += 1

print("fuera del while")