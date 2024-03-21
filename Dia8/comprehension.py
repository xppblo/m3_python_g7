n = 10

lista_pares = [] #lista vacia

for i in range(n) :
    lista_pares.append(2*i +2) #[2,4,6,8,10,12,14,16,18,20]
    
"""  
for i in range(1, n + 1) :
    lista_pares.append(2*i)# [2,4,6,8,10,12,14,16,18,20]
    
for i in range(2,(2*n+2),2) :
    lista_pares.append(i)# [2,4,6,8,10,12,14,16,18,20]
""" 
#[fórmula for variable in iterable]
lista_par = [2*i + 2 for i in range(n)]
print(lista_par)
#append agrega elementos al final de la lista

#[expresión1 if condición1 else expresión2 for variable in iterable]
print("")
valores = [0,4,5,6,7,8,9]
divisibles = []
for valor in valores:
    if valor % 2 == 0:
        divisibles.append('Divisible')
    else:
        divisibles.append('No Divisible')
print(divisibles)

print("")
divisibles2 = ['Divisible' if valor % 2 == 0 else 'No Divisible' for valor in valores ]
print(divisibles2)

print("")

lista = ['Lechugas', 'Tomates', 5, 10, True, False, True, 'Papas', 5.1, 45.2, 1, 2, 0]
count_str = 0
for elemento in lista:
    if type(elemento) is str:
        count_str += 1
print(count_str)

lst_str = [elemento for elemento in lista if type(elemento) is str ]
print(len(lst_str))

#Diccionario comprehension

claves = ['nombre','apellido','edad','altura']
valores = ['Juan','Pérez', 33, 1.75]
diccionario2 = {k:v for k,v in zip(claves, valores)}
print(diccionario2)
