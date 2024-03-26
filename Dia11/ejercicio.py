almacen = {
    "Chocolates" : 10,
    "Papas Fritas" : 20,
    "Bebidas" : 15,
    "Pan" : 10,
    "Mermelada" : 5     
}
print(almacen)

almacen["Helados"] = 12 # Agrega
print(almacen)

almacen["Mermelada"] = 10 # Modifica
print(almacen)

del almacen["Chocolates"] # Elimina
print(almacen)