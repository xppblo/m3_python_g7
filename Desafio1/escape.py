import math


print("Vamos a calcular la velocidad necesario para salir de un planeta, para ello necesitaremos que nos entregues ciertos datos que te pediremos a continuación.")
# radio = radio del planeta
# constanteg = Gravedad del planeta
radio = float(input("Ingrese el radio del planeta en Kilómetros: "))
constanteg = float(input("Ingrese la constante g (gravedad) del planeta: "))

radio = radio * 1000

velocidadEscape = round(math.sqrt(2 * constanteg * radio), 1)


print(f"La velocidad de Escape es: {velocidadEscape} [m/s]")