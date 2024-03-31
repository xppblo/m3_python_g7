
def imprimir_menu():
    print('Opciones: ')
    print('1) De acuerdo')
    print('2) En desacuerdo')
    print('3) No me interesa')
    
def imprimir_respuestas():
    """
    print(f"la respuesta a la pregunta 1 fue : {respuesta[0]}")
    print(f"la respuesta a la pregunta 1 fue : {respuesta[1]}")
    print(f"la respuesta a la pregunta 1 fue : {respuesta[2]}")
    """
    for i in range(len(respuesta)):
        print(f"La respuesta a la pregunta {i+1} fue : {respuesta[i]}")
        
encuesta = ["Encuesta 1", "Encuesta 2", "Encuesta 3"]
respuesta = []

for pregunta in encuesta:
    print(pregunta)
    imprimir_menu() # invoca la funcion
    respuesta.append(input('> '))
    
imprimir_respuestas()