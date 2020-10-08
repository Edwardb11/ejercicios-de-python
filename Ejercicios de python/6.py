#Escriba un programa al cual se le introduzcan diez valores y al final imprima por pantalla
# la suma de los valores, las sumas de los cuadrados, el promedio, el máximo y el mínimo.


numero = int(input("¿Cuantos valores va a introducir?: "))

if numero <= 0:
    print("¡NO es posible!")
else:
    valor = float(input("Escriba el número 1: "))
    minimo = valor
    maximo = valor
    suma = 0
    valor=0
    for a in range(2, numero+1, 1):
        valor = float(input(f"Escriba el número {a}: "))
        suma = suma + valor
        if valor < minimo:
            minimo = valor
        if valor > maximo:
            maximo = valor
        promedio = suma/numero
print(f"El numero más pequeño de los introducidos es {minimo}")
print(f"El numero más grande de los introducidos es {maximo}")
print(f"La suma de los numeros es {suma}")
print(f"El promedio de los numeros es {promedio}")