"""
TUPLAS

Conjunto de datos ordenados e inmutables   
se escriben con parentesis ()
"""

tupla1 = (1,3,5,7,9)
print(tupla1)
print(type(tupla1))#<class 'tuple'>
tupla2 = ("nombre", "Pablo")

nom, texto = tupla2

print(nom,texto)

print(tupla2[0])# nombre
print(tupla2[1])# Pablo
#print(tupla2[2]) IndexError: tuple index out of range

#INMUTABLES
#tupla2[2] = "hola" TypeError: 'tuple' object does not support item assignment
#tupla2[1] = "hola" TypeError: 'tuple' object does not support item assignment

#Iterar tuplas
for num in tupla1:
    print(num)

# cada vez que se quiera transformar un diccionario a una lista, se ocupa el metodo list()
list_dicc1 = list({"nota1":5,"nota2":6}.items())
print(list_dicc1) # dict_items([('nota1', 5), ('nota2', 6)])
print(list_dicc1[0]) # ('nota1', 5)
print(list_dicc1[1]) # ('nota2', 6)

print(list_dicc1[0][0]) # nota1
print(list_dicc1[0][1]) # 5
print(list_dicc1[1][0]) # nota2
print(list_dicc1[1][1]) # 6
