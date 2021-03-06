#Escriba un programa que pregunte cuántos números se van a introducir, pida esos números, y muestre un mensaje cada vez que un número no sea mayor que el anterior.

anterior=0
cantidad  = int(input("¿Cuantos numeros va a introducir?: "))
if cantidad  < 1:
    print("Introduzca un numero mayor que 0: ")
else:
    for a in range(1,cantidad,1):
        anterior = int(input(f"Escriba un número: "))
        numero = int(input(f"Escriba un número más grande que {anterior}: "))
        if numero <= anterior:
            print(f"El numero introducido {numero} No es mayor  {anterior}, por favor introduzca otro numero")
            anterior = numero