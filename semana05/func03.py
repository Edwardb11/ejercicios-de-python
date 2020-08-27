# trabajando con parametros

def sumar(a,b):
    # imprimiendo valores
    print(f"La suma de los valores es {a + b}")

def restar(a,b):
    resultado = a - b
    return(resultado)

    




print("Ingresa los valores")
valor1 = int(input("Primer valor: "))
valor2 = int(input("Segundo valor: "))

# sumar(valor1, valor2)

# recibiendo valor retornado
vresultado = restar(valor1, valor2)
print(vresultado)

print(restar(valor1, valor2))