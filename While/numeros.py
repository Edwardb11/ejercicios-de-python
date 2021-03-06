#Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir). El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.

numero = int(input("Ingresa la cantidad de numeros: "))
num=0
while num < numero :
    a = int(input("Ingresa un numero: "))
    num= num+1
    if a < 0:
        print ("Numero menor que 0")

    elif a>0:
        print("Numero mayor que 0")

    elif a==0:
         print("Numero igual a 0")