# definimos el diccionario
efemerides = {
    '1 de enero': 'Año Nuevo',
    '27 de febrero': 'Terremoto en Chile',
    '8 de marzo': 'Día de la Mujer',
    '21 de mayo': 'Glorias Navales',
    '18 de septiembre': 'Fiestas Patrias',
    '19 de septiembre': 'Glorias del Ejercito',
    '25 de diciembre': 'Navidad'
 }

fecha = input('Ingrese una Fecha:\n').lower()

# en caso de no encontrar la fecha solicitada devolverá el texto indicado
print(f'Efemérides: {efemerides.get(fecha,"No hay eventos para esta fecha")}')
