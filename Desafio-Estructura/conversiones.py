import sys 

Sol_peruano = float(sys.argv[1])
Peso_argentino = float(sys.argv[2])
Dolar_americano = float(sys.argv[3])
Peso_chileno = float(sys.argv[4])

conversion_peru = Sol_peruano * Peso_chileno
conversion_arg = Peso_argentino * Peso_chileno
conversion_usa = Dolar_americano * Peso_chileno

print(f"Los {Peso_chileno} pesos equivalen a: \n {conversion_peru} Soles \n {conversion_arg} Pesos Argentinos \n {conversion_usa} Dólares")
