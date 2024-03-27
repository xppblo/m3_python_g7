recordatorios = [
    ['2021-01-01', "11:00", "Levantarse y ejercitar"],
    ['2021-05-01', "15:00", "No trabajar"],
    ['2021-07-15', "13:00", "No hacer nada es feriado"],
    ['2021-09-18', "16:00", "Ramadas"],
    ['2021-12-25', "00:00", "Navidad"]
    ]

#se agregan fechas
recordatorios.append(['2021-02-02', '06:00', 'Empezar el año'])
recordatorios.append(['2021-12-24', '22:00', 'Cena de Navidad'])
recordatorios.append(['2021-12-31', '22:00', 'Cena de Año Nuevo'])

#cambia la fecha de '2021-07-15' a '2021-07-16'
recordatorios[2][0] = '2021-07-16'

recordatorios_filtrado = []

for evento in recordatorios:
    if evento[2] != "No trabajar":
        recordatorios_filtrado.append(evento)

recordatorios = recordatorios_filtrado
        
#Ordena la lista por fechas
recordatorios.sort()

# Output
print(recordatorios)
