#Elabore un programa que pida un número entero por pantalla e imprima todos los números
#  que lo dividen exactamente. El programa debe controlar que los valores digitados sean 
# positivos. En caso de haber digitado un negativo, debe dar un mensaje de error. Ejemplo: 
#Input: 6
#Output: 6, 3 y 2.


print("DIVISORES")
numero = int(input("Escriba un número entero mayor que cero: "))

if numero <= 0:
     print("No puedes introducir un numero negativo")
else:
    print(f"Los divisores de {numero} son ", end="")
    for i in range(1, numero + 1):
        if numero % i == 0:
            print(i, end=" ")
