#09
primos = 0
spam = 1
divExac = 0
modulo = 0
esprimo = ""
listprimos = []
cantidad = int(input("Digite la cantidad de numeros primo que desea: "))
contador = int(input("¿Apartir de que numero desea que inicie la busqueda? "))
print ("---------------------------------------------------------------------")
print(f"El listado de {cantidad} numeros primos a partir del numero {contador} es: ")
 
while True :
    if primos == cantidad:
        break
    if primos > cantidad:
        break
# opracion para determinar si contador es primo, sera primo si solo tiene dos divisores exactos
    spam = 1
    divExac = 0
    while spam <= contador:
        modulo = contador%spam
        if modulo == 0:         #determinar si el es divisor exacto
            divExac += 1        #cuantos divExac tuvo el contador
        spam += 1   
 
# si se hayo un primo, incrementa primo de lo contrario solo umenta el contador
    if divExac == 2:
        primos +=1
        listprimos.append(contador)
    contador +=1
 
print(f"{listprimos}")
print ("---------------------------------------------------------------------")
print ("El programa a concluido, gracias por elegirnos \n")


