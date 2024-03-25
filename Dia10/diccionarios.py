"""
Estructura de datos pares clave:valor

Permiten guardar una gran cantidad de datos en una sola variable
se accede a los elementos a traves de la clave, no importa la posicion
las claves no se generan automaticamente
las claves pueden ser str, numericos(int), boolean
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