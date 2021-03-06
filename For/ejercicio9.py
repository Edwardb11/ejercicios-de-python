#Escriba un programa que pida dos números enteros y escriba la suma de todos los enteros desde el primer número hasta el segundo.

valor1= int(input("ingresa un numero entero positivo: "))
if valor1 <= 0:
    print("le he pedido un numero positivo")
else:
    valor2 = int(input(f"escriba un numero entero mayor que {valor1}: "))
    if valor2 <= valor1:
        print(f"por favor ingresa un numero entero mayor que {valor1}")
    else:
        suma = 0
        for x in range(valor1 + valor2 + 1):
            suma= suma + x
            print(f"La suma desde {valor1} hasta {valor2} es: {suma}")


