"""
() -> tuplas
{} -> diccionarios
[] -> listas

LISTAS

son contenedores de datos, son mutables
conjunto de datos, separados por coma y ordenados segun su ingreso
la primera posición (INDICE) es CERO

"""

lista_pares = [2, 4, 6, 8, 10]

print(lista_pares)

print(len(lista_pares))

print("")

#indice o posicion
print(lista_pares[0])# 2
print(lista_pares[1])# 4
print(lista_pares[2])# 6
print(lista_pares[3])# 8
print(lista_pares[4])# 10
#print(lista_pares[5]) IndexError: list indext out of range

print("")
lista_vacia=[] # lista vacia de 0 elementos

print(lista_pares[-1])# 10
print(lista_pares[-2])# 8

print(lista_pares.__dir__) #<built-in method __dir__ of list object at 0x0000016367EDD900>
print(lista_pares.__dir__())
print("")
# append(dato) -> agrega un elemento al final de la lista

#insert(indice,dato) -> inserta un elemento en la posición indicada
lista_vacia.append("Lunes")
print(lista_vacia)
lista_vacia.append("Martes")
print(lista_vacia)
lista_vacia.append("Miercoles")
print(lista_vacia)
lista_vacia.insert(3,"Jueves")# ['Lunes', 'Martes', 'Miercoles', 'Jueves']
print(lista_vacia)
lista_vacia.insert(3,"Viernes")# ['Lunes', 'Martes', 'Miercoles', 'Viernes', 'Jueves']
print(lista_vacia)

print("")
lista_vacia[3] = "Jueves" #-> remplaza un elemento en esa posición
lista_vacia.insert(10,"Sabado")
print(lista_vacia)

print("")
#pop() -> saca el ultimo elemento dentro de la lista

lista_vacia.pop(4)#['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Sabado']
print(lista_vacia)
#lista_vacia.pop(0)#['Martes', 'Miercoles', 'Jueves', 'Sabado']
#print(lista_vacia)

lista_eliminados = []
lista_eliminados.append(lista_vacia.pop(0))

print("")

lista_vacia.remove("Martes")
print(lista_vacia)
#lista_vacia.remove("Viernes")# ValueError: list.remove(x): x not in list
#print(lista_vacia)
lista_vacia.append("Jueves")
print(lista_vacia)
lista_vacia.remove("Jueves") #Elimina la primera coincidencia
print(lista_vacia)

print("")

#reverse() -> invierte los elementos de la lista, el cambio es permanente

lista_vacia.reverse()# ['Jueves', 'Sabado', 'Miercoles']
print(lista_vacia)

print("")

#sort() -> ordena la lista de forma ascendente / numericamente

lista_vacia.sort()
print(lista_vacia)

print("")

#RESPALDO DE LISTAS

lista1 = lista_pares#NO ES UN RESPALDO DE DATOS

lista2 = lista_pares.copy() # Crea un resplado de la lista original
lista3 = lista_pares[:] # crea un respaldo de la lista original
lista4 = lista_pares + [] # crea un respaldo de la lista original
lista5 = lista_pares *1 # crea un respaldo de la lista original
lista6 = list(lista_pares) # crea un respaldo de la lista original

lista_pares.pop()
print("La lista de pares", lista_pares)
print(lista1)

lista_pares.pop()
print("lista de pares",lista_pares)
print(lista1)
print(lista2)
print(lista3)
print(lista4)
print(lista5)
print(lista6)


#sorted(lista, reverser= True)
#sorted(lista_pares, reverse= True) -> el sorted debe estar dentro de un print
print(sorted(lista_pares, reverse= True)) #-> True ordena descendente, False ordena ascendente

#index()-> retorna el indice del elemento que se busca en la lista
print("indice del elemento 4 es :", lista_pares.index(6))
#print("indice del elemento 4 es :", lista_pares.index(500)) # ValueError: 500 is not in list

lista_final = lista_pares + lista_vacia
print(lista_final)