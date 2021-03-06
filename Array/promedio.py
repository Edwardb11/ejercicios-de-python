#Realizar un programa que solicite diez números, los almacene en un array y luego calcule el promedio de esos números.

numeros = []
for x in range (10):
    numeros.append(int(input("Introduce un numero:")))
print(sum(numeros)/int(len(numeros)))