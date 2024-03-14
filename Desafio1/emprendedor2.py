
print("Para calcular las utilidades necesitaremos que nos proporciones algunos datos.")

precioSuscripcion = float(input("Ingresa el valor de las suscripcion:\n"))
numeroUsuariosNormal = int(input("Ingresa el número de usuarios normales:\n"))
numeroUsuariosPremium = int(input("Ingresa el número de usuarios premium:\n"))
gastosTotales = float(input("Ingresa el valor de los gastos totales:\n"))

precioSuscripcionPremium = float(precioSuscripcion * 1.5)


utilidades = round((precioSuscripcion * numeroUsuariosNormal) + (precioSuscripcionPremium * numeroUsuariosPremium) - gastosTotales)

print(f"Las utilidades del negocio son: {utilidades}")