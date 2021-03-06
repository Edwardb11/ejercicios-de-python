#Haga una función tipoTriang(a, b, c) a la cual se le pase como parámetros las longitudes de los lados y 
# retorne 1, 2 o 3 según el triángulo sea equilátero, isósceles o escaleno.

def triang(a,b,c):
    if a==b and a ==c:  #Si son iguales entonces son equilateros
        return "Equilatero"
    elif a!=b and a!=c:
        return "Escaleno" #Cuando todos los lados son diferentes
    else:
        return "Isosceles" #SI no es ninguno de los anteriores entonces es isosceles

print(triang(7,7,7))