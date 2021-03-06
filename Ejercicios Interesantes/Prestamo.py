#4)Un prestamista necesita un programa que le permita introducir los siguientes datos de los préstamos que otorga:
#  número de préstamo, fecha, cliente, Capital (monto)prestado y  tiempo. Sabiendo que presta a un 7% de interés,
#a)calcule y muestre a cuánto equivalen la amortización del préstamo (monto que se debe pagar para reducir 
# el capital prestado), el monto de interés y el monto de la cuota a pagar cada mes.

#b)Si se penaliza con un 3.5% de mora por día (cuando el cliente no paga en la fecha indicada); cuánto debería pagar 
# de interés, mora y cuota un cliente que se pasó por 4 días de la fechanormal de pago? Presente todos los resultados 
# de los cálculos realizados.
def prestamo():
    numeroP=int(input("Introduzca el numero de prestamo: "))
    fecha=input("Introduzca la fecha:")
    cliente=input("Ingrese su nombre: ").capitalize()
    capital=int(input("Introduzca el monto$: "))
    tiempo=int(input("Introduzca el tiempo de plazo (En meses): "))

    itebis= (capital*7)/100 +capital
    PagarM=itebis/tiempo
    interes=itebis-capital
    calcular=(itebis*0.035)/4
    print(f"Datos sobre el prestamo numero {numeroP} otorgado a {cliente} el {fecha}")
    print(f"El total a pagar es: {itebis}")
    print(f"El interes para su prestamo es de: {interes}")
    print(f"Pagara mensual: {PagarM}")

    print("En caso de que se halla pasado de la fecha indicada\nPagara: ",calcular+itebis)

print(prestamo())