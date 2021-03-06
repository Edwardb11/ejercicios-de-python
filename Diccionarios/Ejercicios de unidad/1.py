#Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, 
# pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en 
# el diccionario.

Diccionario= {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
Preguntar = input("Introduce una divisa: ")
#if Preguntar in Diccionario:
    #print(Diccionario.get(Preguntar))
#else: 
    #print("La divisa no está.")
print(Diccionario.get(Preguntar.title(), "La divisa no está."))