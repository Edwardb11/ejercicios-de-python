#Escribir un programa que pregunte al usuario los números ganadores de la lotería nacional, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
numeros = []
for x in range (3):
    numeros.append(int(input("¿Cuales son los numeros ganadores?: ")))
numeros.sort ()
print(numeros)


    

