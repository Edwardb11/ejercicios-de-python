#Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma y la media de todos los números introducidos.

suma=0
cont=0
num=int(input("Numero:"))
while num!=0:
     cont=cont+1
     suma=suma+num
     num=int(input("Numero:"))
media=float(suma)/cont
print ("La suma es %d y la media es %f"%(suma,media))
