import sys

precios = {
    'Notebook': 700000,
    'Teclado': 25000,
    'Mouse': 12000,
    'Monitor': 250000,
    'Escritorio': 135000,
    'Tarjeta de Video': 1500000
    }

def filtrar_productos(precios, umbral, operacion = 'mayor'):
    
    if operacion == 'mayor':
        productos_filtrados = []
        for producto, precio in precios.items():
            if precio > umbral:
                productos_filtrados.append(producto)
    elif operacion == 'menor':
        productos_filtrados = []
        for producto, precio in precios.items():
            if precio < umbral:
                productos_filtrados.append(producto)
    else:
        return "Lo sentimos, no es una operación válida"

    return f"Los productos {operacion}es al umbral son: {', '.join(productos_filtrados)}"

if len(sys.argv) == 2:
    umbral = int(sys.argv[1])
    print(filtrar_productos(precios, umbral))
elif len(sys.argv) == 3:
    umbral = int(sys.argv[1])
    operacion = sys.argv[2]
    print(filtrar_productos(precios, umbral, operacion))
    

