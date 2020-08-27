# manejo de excepciones 

def dividir(valor1, valor2):
    try:
       return valor1 / valor2 
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero")
    


numero1 = 42
numero2 = 0

resultado = dividir(numero1, numero2)

print(resultado)

