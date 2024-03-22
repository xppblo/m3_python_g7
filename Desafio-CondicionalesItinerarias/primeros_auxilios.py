import sys

print("Preguntas basicas para realizar primeros auxilios, por favor conteste las preguntas con un Si o No")

estimulos = input("La persona responde a estimulos? Si / No\n").lower()

if estimulos != "si" :
    print("Abrir la via Aerea")
else :
    print("Valorar la necesidad de llevarlo al hospital mas cercano")
    sys.exit()

respira = input("La persona Respira? Si / No\n").lower()

if respira != "si" :
    print("Administrar 5 ventilaciones y llamar a la ambulancia")
else :
    print("Permitirle posicion de suficiente ventilacion")
    sys.exit()

ambulancia = "no"

while ambulancia != "si" :
    signos_vida = input("Tiene signos vitales? Si / No\n")
    if signos_vida == "si" :
        print("Reevaluar a la espera de la ambulancia")
        ambulancia = input("LLego la ambulancia? Si / No\n").lower()
    else :
        print("Administrar compresiones toracicas hasta que llegue ambulancia")
        ambulancia = input("LLego la ambulancia? Si / No\n").lower()

print("Fin del programa")