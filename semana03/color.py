# Realizar un algoritmo que pida al usuario digitar un color y lo muestre, pero cuando el usuario digita el color rojo se termine y lo indica.

color = input("Ingrese un color: ")
while color != "Rojo":
    print(f"El color {color} es incorrecto")
    color = input("Ingrese un color: ")
print("Programa finalizado")




     
     