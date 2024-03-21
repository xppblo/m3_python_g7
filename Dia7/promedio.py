
cant_notas = int(input("Ingrese la cantidad de notas que deseas promediar:\n"))

i = 0
suma_notas = 0

while i < cant_notas :
    nota = float(input("Ingresa tu nota :\n"))
    suma_notas = suma_notas + nota
    i += 1
    
print(f"El primedio de notas es : {round(suma_notas/cant_notas,2)}")