#Escribir una función que reciba un número entero positivo y devuelva su factorial.

def factorial(n):
    valor= 1
    for x in range (n):
        valor *= x+1 
    return valor
print(factorial(5))
