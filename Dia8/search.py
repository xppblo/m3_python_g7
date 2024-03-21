import sys, random

numero_buscar = int(sys.argv[1])

lista = [1,2,3,4,5,6,7,8,9,0]
random.shuffle(lista) # Desordena la lista de foram permanente
print(lista)

for posicion, numero in enumerate(lista):
    
    if numero_buscar == numero:
        print(f"El numero {numero_buscar} se encontro en la posicion {posicion}")
        break
    else:
        # Si es que no es el elemento buscado lo reportamos
        print(f"Elemento no se encontro en la posicion {posicion}")
    
print("Fin del programa")