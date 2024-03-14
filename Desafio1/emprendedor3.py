print("Para calcular las utilidades necesitaremos que nos proporciones algunos datos.")

precioSuscripcion = float(input("Ingresa el valor de las suscripcion:\n"))
numeroUsuarios = float(input("Ingresa el número de usuarios:\n"))
gastosTotales = float(input("Ingresa el valor de los gastos totales:\n"))
utilidadesAnterior = float(input("Ingrese las utilidades del año anterior:\n"))

utilidades = round(precioSuscripcion * numeroUsuarios - gastosTotales)

razonUtilidades = round((utilidades / utilidadesAnterior), 2)

print(f"Las utilidades del negocio son: {utilidades}")
print(f"La razón entre las ultimas utilidades y las del año anterior son: {razonUtilidades}")