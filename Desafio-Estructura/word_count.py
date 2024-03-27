with open('lorem_ipsum.txt', "r") as file:
    texto = file.read()

#Contador de letras
letras = set(texto)
letras_distintas = len(letras)

#Contador de palabras
palabras = texto.split()
palabras_distintas = set(palabras)
cont_palabras_distintas = len(palabras_distintas)

print(f"El número de letras distintas es: {letras_distintas}")
print(f"El número de palabras distintas es: {cont_palabras_distintas}")
