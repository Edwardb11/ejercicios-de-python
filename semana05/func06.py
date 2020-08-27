# numeros aleatorios
import random
numeroSecreto = random.randint(1, 20)
print("Piensa en un numero entre 1 al 20")

# tener 6 oportunidades para encontrar respuesta

def ProgramaAleatorio():
    for numeroIntentos in range(1,7):
        print("Ingresa una opcion")
        respuesta = int(input())

        if respuesta < numeroSecreto:
            print("El valor ingresado esta por debajo del numero")
        elif respuesta > numeroSecreto:
            print("El valor ingresado esta por encima del numero")
        else:
            break

    if respuesta == numeroSecreto:
        print(f"Buen trabajo has adivinado en {numeroIntentos} intento, felicidades!!")
    else:
        print(f"A sobrepasado el numero de intentos, el numero secreto era {numeroSecreto}")

ProgramaAleatorio()