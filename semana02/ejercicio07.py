valor1 = int(input('registra un valor'))
valor2 = int(input('registra un valor'))
valor3 = int(input('registra un valor'))

if (valor1 >= valor2) and (valor1 >= valor3):
    numero3 = valor1

    if (valor2 >= valor3):
        numero2 = valor2
        numero1 = valor3
    else:
        numero2 = valor3
        numero1 = valor2

elif (valor2 >= valor1) and (valor2 >= valor3):
    numero3 = valor2

    if (valor1 >= valor3):
        numero2 = valor1
        numero1 = valor3
    else:
        numero2 = valor3
        numero1 = valor1
        
elif (valor3 >= valor1) and (valor3 >= valor2):
    numero3 = valor3
    
    if (valor1 >= valor2):
        numero2 = valor1
        numero1 = valor2
    else:
        numero2 = valor2
        numero1 = valor1

print(f"El valor mas bajo es {numero1}")
print(f"El valor del medio es {numero2}")
print(f"El valor mas alto es {numero3}")
