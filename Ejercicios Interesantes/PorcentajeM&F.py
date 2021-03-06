#Determinar porcentaje de hombre y mujeres
Femenino=0
Masculino=0
Mujeres=int(input('Digite el numero de mujeres: '))
Hombres=int(input('Digite el numero de hombres: '))
while Mujeres > 0 and Hombres >0:
    Femenino+=Mujeres/100
    Masculino+=Hombres/100
    print( "{}%".format(Femenino))
    print( "{}%".format(Masculino))
    break