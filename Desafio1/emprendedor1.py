#import math

print("Para calcular las utilidades necesitaremos que nos proporciones algunos datos.")

precioSuscripcion = float(input("Ingresa el valor de las suscripcion:\n"))
numeroUsuarios = int(input("Ingresa el número de usuarios:\n"))
gastosTotales = float(input("Ingresa el valor de los gastos totales:\n"))

utilidades = round(precioSuscripcion * numeroUsuarios - gastosTotales)

print(f"Las utilidades del negocio son: {utilidades}")