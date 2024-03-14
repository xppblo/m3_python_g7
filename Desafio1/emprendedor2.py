
print("Para calcular las utilidades necesitaremos que nos proporciones algunos datos.")

precioSuscripcion = float(input("Ingresa el valor de las suscripcion:\n"))
numeroUsuariosNormal = float(input("Ingresa el número de usuarios normales:\n"))
numeroUsuariosPremium = float(input("Ingresa el número de usuarios premium:\n"))
gastosTotales = float(input("Ingresa el valor de los gastos totales:\n"))

precioSuscripcionPremium = precioSuscripcion
precioSuscripcionPremium = float(precioSuscripcionPremium + (precioSuscripcion * 0.5))


utilidades = round((precioSuscripcion * numeroUsuariosNormal) + (precioSuscripcionPremium * numeroUsuariosPremium) - gastosTotales)

print(f"Las utilidades del negocio son: {utilidades}")