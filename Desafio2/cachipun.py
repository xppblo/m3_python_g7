import random
import sys

print("Vamos a jugar al cachipun para ello deberas elejir una de las siguientes opciones Piedra, Papel o Tijeras")

opciones = ['Piedra', 'Papel','Tijeras']
jugador1 = input(f"Elige {opciones} \n")

computador = random.choice(opciones)

if jugador1 == "Piedra" :
    print(f"Tu eleccion es {jugador1}")
elif jugador1 == "Papel" :
    print(f"Tu eleccion es {jugador1}")
elif jugador1 == "Tijeras" :
    print(f"Tu eleccion es {jugador1}")
else :
    print(f"Solo puedes escojer una de las siguientes {opciones}")
    sys.exit()

if jugador1 == "Piedra" and computador == "Tijeras" :
    print(f"Elejiste {jugador1} y la computadora eligio {computador}, Ganaste")
elif jugador1 == "Piedra" and computador == "Papel" :
    print(f"Elejiste {jugador1} y la computadora eligio {computador}, Perdiste")
elif jugador1 == "Papel" and computador == "Piedra" :
    print(f"Elejiste {jugador1} y la computadora eligio {computador}, Ganaste")
elif jugador1 == "Papel" and computador == "Tijeras" :
    print(f"Elejiste {jugador1} y la computadora eligio {computador}, Perdiste")
elif jugador1 == "Tijeras" and computador == "Piedra" :
    print(f"Elejiste {jugador1} y la computadora eligio {computador}, Perdiste")
elif jugador1 == "Tijeras" and computador == "Papel" :
    print(f"Elejiste {jugador1} y la computadora eligio {computador}, Ganaste")
else :
    print(f"Ambos elijieron la opción {jugador1}, es un Empate")