a = [100, 200, 1000, 5000, 10000, 10, 5000]
n = len(a)
filtered_array = []
for i in range(n):
    if a[i] >= 1000:
        filtered_array.append(a[i])
print(filtered_array)

filtered_array2 = [a[i] for i in range(n) if a[i]>= 1000]
print(filtered_array2)

#Ejercicio 2
minutos = [120, 50, 600, 30, 90, 10, 200, 0, 500]

lista_minutos = ['bueno' if i < 90 else 'malo' for i in minutos]
print(lista_minutos)

#Ejercicio 3
seconds = [100, 50, 1000, 5000, 1000, 500]

transformer_minutos = [seconds[i]/60 for i in range(n)]