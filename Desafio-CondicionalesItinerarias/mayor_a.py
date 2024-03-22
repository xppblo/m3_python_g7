import sys

ventas = {
 "Enero": 15000,
 "Febrero": 22000,
 "Marzo": 12000,
 "Abril": 17000,
 "Mayo": 81000,
 "Junio": 13000,
 "Julio": 21000,
 "Agosto": 41200,
 "Septiembre": 25000,
 "Octubre": 21500,
 "Noviembre": 91000,
 "Diciembre": 21000,
}

ventas_filtrado = {}



i = int(sys.argv[1])

for clave,valor in ventas.items() :
    if valor > i :
        ventas_filtrado[clave] = valor
print(ventas_filtrado)

ventas_filtrado2={clave:valor for clave,valor in ventas.items() if valor > i}

print(ventas_filtrado2)