mascotas= {}

cant_mascotas = int(input("Ingrese la contidad de mascotas a ingresar : \n"))#3

for i in range(cant_mascotas):

    mascota = {
        "nombre" : "",
        "raza" : "",
        "anillado" : False ,
        "peso" : 0.0 ,
        "altura" : 0.0 ,
        "edad" : 0
    }


    # Recorrer un diccionario default
    #for clave in mascota:
    #    print(clave)
    #    mascota[clave] = input(f"Ingrese {clave} de su mascota : \n")
    #print(mascota)

    for key in mascota.keys():
        print(key)
        mascota[key] = input(f"Ingrese {key} de su mascota : \n")
    print(mascota)

    print("")
    for valor in mascota.values():
    #accedemos a los valores de nuestro diccionario
        print(valor)
        
    for key,value in mascota.items():
        print(f"clave {key} - valor {value}")
        
        
    mascotas[mascota["nombre"]] = mascota 
print(mascotas)

"""
mascotas = {
    'Blue' : {'nombre': 'Blue', 'raza': 'Agapornis', 'anillado': 'Si', 'peso': '0.9', 'altura': '0.15', 'edad': '3'}
}

mascotas["Blue"]["nombre"] => "nombre" : "Blue"
mascotas["Blue"].pop("nombre") -> Elimina nombre del diccionario de Blue
"""
    