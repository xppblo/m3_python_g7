
print("En esta aplicación calcularemos su indice de masa corparl para ello necesitaremos su peso y su altura")

peso = float(input("Ingrese su peso en kg :\n"))
altura = float(input("Ingrese su altura en cm :\n"))

if altura <= 0 :
    print("Debe ingresar una altura valida")
else :
    altura = altura / 100

    imc = peso / (altura**2)

    imc = 35

    if imc < 18.5 :
        print(f"Su IMC es {imc:.2f}, y se encuentra bajo peso")
    elif imc <= 18.5 or imc < 25 :
        print(f"Su IMC es {imc:.2f}, y su peso es Adecuado")
    elif imc <= 25 or imc < 30 :
        print(f"Su IMC es {imc:.2f}, y su peso es Sobrepeso")
    elif imc <= 30 or imc < 35 :
        print(f"Su IMC es {imc:.2f}, y su peso es Obesidad Grado I")
    elif imc <= 35 or imc < 40 :
        print(f"Su IMC es {imc:.2f}, y su peso es Obesidad Grado II")
    else:
        print(f"Su IMC es {imc:.2f}, y su peso es Obesidad Grado III")

print("Fin del programa")
