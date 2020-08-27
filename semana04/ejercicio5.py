#Escriba un programa que pida un número entero mayor que cero y que escriba sus divisores.

print ("Escribe un numero mayor que cero")
numeros= int(input("Ingrese un numero: "))
salida = ''

for i in range(1,numeros+1):
    if (numeros %i == 0):
        salida = salida +' ' + str (i)
        
print (f"Los divisores de {numeros} son {salida}")