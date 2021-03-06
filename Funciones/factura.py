#Escribir una función que calcule el total de una factura tras aplicarle el ITEBIS. La función debe recibir la cantidad 
#sin ITEBIS y el porcentaje de ITEBIS a aplicar,  y devolver el total de la factura. Si se invoca la función sin pasarle 
#el porcentaje de ITEBIS, deberá aplicar un 18%.

def  factura (cantidad, itebis):
    if (itebis >0):
        suma= (cantidad*itebis)/100+cantidad
        return suma
    else:
        suma= (cantidad*18)/100+cantidad
    return suma

cantidad= int(input("Ingresa la cantidad : "))
itebis= int(input("Ingresa el itebis: "))
print(factura(cantidad,itebis))