#Escriba un programa que pregunte cuantos números se van a introducir, pida esos números (que puedan ser decimales) y calcule su suma.

numero = int(input("¿Cuantos numeros va a introducir?"))
suma= 0

for x in range(1,numero+1):
    if numero <= 0:
        print("no es posible")
    else:
        cantidad = float(input(f"escriba el numero {x}: "))
        suma= suma + cantidad
print(f"La suma de los numeros es {suma}")
    



       