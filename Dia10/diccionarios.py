"""
Estructura de datos pares clave:valor

Permiten guardar una gran cantidad de datos en una sola variable
se accede a los elementos a traves de la clave, no importa la posicion
las claves no se generan automaticamente
las claves pueden ser str, numericos(int), boolean
si la clave existe la modifica y si no existe se agrega
"""

diccionario = {
    1: "uno",
    "dos": 2,
    3: [1,2,3,4,5,6],
    "dicc" : {"A":"A mayuscula"}
    }

notas = {
"Camila": 7,
"Antonio": 5,
"Felipe": 6,
"Daniela": 5,
"Vicente": 7,
"FELIPE":2,
"Vicente":1 #la clave se repiten, simpre sera remplazado con ultimo valor ingresado, ya que no pueden existir claves con el mismo valor
}

print(len(notas))# 5
print(notas)#{'Camila': 7, 'Antonio': 5, 'Felipe': 6, 'Daniela': 5, 'Vicente': 7}

#Acceder a los valores a traves de la clave
print(notas["Camila"])
print(notas["Antonio"])
print(notas["Felipe"])
print(notas["Daniela"])
print(notas["Vicente"])

notas["Julio"] = 5

print(notas)#{'Camila': 7, 'Antonio': 5, 'Felipe': 6, 'Daniela': 5, 'Vicente': 7

#modificar par clave valor
notas["Julio"] = 7
print(notas)

#eliminar par clave:valor
del notas["FELIPE"] # elimina a FELIPE
print(notas) #{'Camila': 7, 'Antonio': 5, 'Felipe': 6, 'Daniela': 5, 'Vicente': 1, 'Julio': 7}

print("")
#Tambien se puede elminar con el pop() -> elimina el valor y lo captura
eliminado = notas.pop("Camila")
print(eliminado)# valor eliminado 7
print(notas) #{'Antonio': 5, 'Felipe': 6, 'Daniela': 5, 'Vicente': 1, 'Julio': 7}

print("")
notas2 = {
    "Miquella" : 7,
    "Malenia" : 5,
    "Radhan" : 6,
    "Felipe" : 3
}

#notas.update(notas2)#{'Antonio': 5, 'Felipe': 6, 'Daniela': 5, 'Vicente': 1, 'Julio': 7, 'Miquella': 7, 'Malenia': 5, 'Radhan': 6}se adiciona notas2 a notas
#print(notas)
notas2.update(notas) #{'Miquella': 7, 'Malenia': 5, 'Radhan': 6, 'Antonio': 5, 'Felipe': 6, 'Daniela': 5, 'Vicente': 1, 'Julio': 7} se adiciona notas a notas2
print(notas2)
#COLICONES : en caso de tener las mismas claves en los diccionarios al hacer update() se remplaza el antiguo valor por el que se esta agregando