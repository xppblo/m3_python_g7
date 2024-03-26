"""
SETS

Conjunto de datos que no permite duplicados, no es ordenado y se escriben con llave {}
entregan el dato unico, se puede modificar
"""


muchos_animales = {'Gato', 'Perro', 'Tortuga',
'Gato', 'Perro', 'Tortuga',
'Gato', 'Perro', 'Tortuga',
'Gato', 'Perro', 'Tortuga',
'Hurón', 'Hamster', 'Erizo de Tierra'}

for i in muchos_animales:
    print(i)

print(muchos_animales) # {'Hurón', 'Erizo de Tierra', 'Gato', 'Tortuga', 'Hamster', 'Perro'} entrega el dato unico

muchos_animales.add("Rinoceronte")
print(muchos_animales) # {'Perro', 'Hurón', 'Erizo de Tierra', 'Tortuga', 'Rinoceronte', 'Gato', 'Hamster'}
#print(muchos_animales("Gato"))  TypeError: 'set' object is not callable
#print(muchos_animales["Gato"]) TypeError: 'set' object is not subscriptable

muchos_animales.remove("Gato") # Se remueven solo claves que existen
#muchos_animales.remove("Leon")  KeyError: 'Leon' -> no se puede eliminar una clave que no existe
print(muchos_animales)

#discard() -> si existe lo quita del set, si no no hace nada
muchos_animales.discard("Leon") # {'Tortuga', 'Rinoceronte', 'Erizo de Tierra', 'Hamster', 'Perro', 'Hurón'}
muchos_animales.discard("Perro") # {'Tortuga', 'Rinoceronte', 'Erizo de Tierra', 'Hamster', 'Hurón'}
print(muchos_animales)

#pop() -> elimina un elemento al azar
muchos_animales.pop()
print(muchos_animales)

#clear() -> quita todos los elementos dentro del set
muchos_animales.clear()
print(muchos_animales)

