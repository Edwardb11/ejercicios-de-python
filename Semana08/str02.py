#manejando str como listas
letras = "La tarea estuvo muy dificil"
print(letras)
print(letras[0])
print(letras[20])
print(letras[0:]) #Imprimeme de la posision 0 en adelante
print(letras[0:7]) #Imprimeme hasta la 7
print(letras[7:]) #Imprimeme desde la 7 en adelante
print("H" in letras)
print(letras.upper())
print(letras.lower())

nombre = "edward brito diaz"
print(nombre.istitle()) #me devuelve falso poque esta en minuscula

#evaluar si una variable esta escrita todo minuscula o mayuscula
print(nombre.isupper()) #Mayuscula
print(nombre.islower()) #Minuscula
