valor1 = float(input("Ingresa un valor: "))
valor2 = float(input("Ingresa un valor: "))
print("Operaciones: Suma (S) | Resta (R) | Multiplicar (M) | Dividir (D) Exponenciacion (E)")
operador = input("Ingresa la operacion a realizar: ")

if operador.upper() == 'S':
    resultado = valor1 + valor2
    print(f"Elegiste Suma")
    print(f"El resultado de la operacion es {resultado}")

elif operador.upper() == 'R':
    resultado = valor1 - valor2
    print(f"Elegiste Resta")
    print(f"El resultado de la operacion es {resultado}")

elif operador.upper() == 'M':
    resultado = valor1 * valor2
    print(f"Elegiste Multiplicar")
    print(f"El resultado de la operacion es {resultado}")

elif operador.upper() == 'D':
    if valor2 == 0:
        print("El valor introducido es invalido")
    else:            
        resultado = valor1 // valor2
        print(f"Elegiste Dividir")
        print(f"El resultado de la operacion es {resultado}")

elif operador.upper() == 'E':
    resultado = valor1 ** valor2
    print(f"Elegiste Exponenciacion")
    print(f"El resultado de la operacion es {resultado}")

else:
    print("Valor Introducido es Incorrecto")    