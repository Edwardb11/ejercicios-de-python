#Escriba un programa que pregunte cuántos números se van a introducir, pida esos números, y diga al final cuántos han sido pares y cuántos impares.

numeros = int(input("¿Cuantos numeros va a introducir? "))
pares = 0
impares = 0

for a in range(1, numeros,1):
    numero= int(input(f"ingrese el valor {a}:"))
    if numero %2 == 0:
        pares= pares +1
    else:
        impares = impares +1
print(f"Has ingresado {pares} numeros pares y {impares} numeros impares")




