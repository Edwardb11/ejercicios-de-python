#Escribe un programa que pida el limite inferior y superior de un intervalo. Si el límite inferior es mayor que el superior lo tiene que volver a pedir. A continuación se van introduciendo números hasta que introduzcamos el 0. Cuando termine el programa dará las siguientes informaciones:

#La suma de los números que están dentro del intervalo (intervalo abierto).
#Cuantos números están fuera del intervalo.
#He informa si hemos introducido algún número igual a los límites del intervalo.

n=0
suma=0
limfue=0
limigu=0
limsup=0
liminf=0
while (limsup <= liminf):
     limsup=int(input("Ingrese el limite superior: "))
     liminf=int(input("Ingrese el limite inferior: "))
while (limsup> liminf):
    n=int(input("Ingrese un numero: "))
    if (n>liminf and n<limsup):
        suma =suma +n
    elif (n== liminf or n== limsup):
        limigu=limigu+1
    else:
        limfue=limfue+1
    if (n==0):
        print(f"La sumas en el intervalo es = {suma} el total de numeros fuera del intervalo es {limfue}")
        break