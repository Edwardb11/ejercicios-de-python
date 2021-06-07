# generador de numeros de loto aleatorio
import random

n = int(input("Ingrese cuantos numeros aleatorios desea obtener"))

print("Los numeros afortunados son: ")
aleatorios = [random.randint(0, 40) for _ in range(n)]
print("Numeros: ", aleatorios)

print("Numero adicional: ", random.randint(0, 10))
