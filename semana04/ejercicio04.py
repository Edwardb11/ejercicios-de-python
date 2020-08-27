#Elabora un algoritmo que solicite la edad de 20 personas y que muestre cuantos son mayores y menores de edad.

x=0
mayor= 0
for a in range (1,21,1):
    edad= int(input("Ingresa la edad: "))
    if edad <=18:
        x= x + 1
    else:
        mayor = mayor + 1
print(f"La cantidad de personas mayor de edad son {mayor} and menores {x}")









