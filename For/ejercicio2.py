#Realizar un algoritmo que solicite un número y luego genere su tabla de multiplicar desde el 1 hasta el 10.

numero = int(input("Introduce un numero: "))
print(f"La tabla de multiplicar {numero} es:")
 
for a in range(1,11,1):
    print(f"{numero} X {a} = {numero*a}")


