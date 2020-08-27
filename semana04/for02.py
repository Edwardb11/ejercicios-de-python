# programa que sume todos los numeros del 0 100

# acumulador
total = 0
repetir = int(input("Introducir Limite: "))

# la variable num es el contador
for num in range(repetir):
    print(f"El valor de num es: {num}")
    total = total + num
    print(f"El valor de total es {total}")
    if num == 3:
        break

print(f"El total de los numeros es: {total}")

