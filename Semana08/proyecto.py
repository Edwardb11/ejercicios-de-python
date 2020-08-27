import random
import string

while True:
    print("--Proyecto: Gestor de Contraseñas--")
    minus=int(input("Indique número mínimo de minusculas: "))
    mayus=int(input("Indique número mínimo de mayusculas: "))
    numeros=int(input("Indique número mínimo de caracteres numéricos: "))
    longitud=int(input("Indique longitud de la contraseña: "))
    suma=minus+mayus+numeros #SUMA DE MINIMOS
    while longitud<suma or longitud <8: #COMPROBACION ADECUACIÓN DE LA "longitud".
        longitud=int(input("Longitud inadecuada: "))
    caract=string.ascii_letters+string.digits  # string.ascii_letters = Devuelve todas las letras ASCII 
    #(tanto en minúsculas como en mayúsculas)
    # string.digits= Devuelve todas las letras de los dígitos.

    while True:
        contra=("").join(random.choice(caract)for i in range(longitud))
        if(sum(c.islower() for c in contra)>=minus
            and sum(c.isupper() for c in contra)>=mayus
            and sum(c.isdigit() for c in contra)>=numeros):
            break
        
    print(f"\nSU CONTRASEÑA: {contra}")
    
    continuar = input("Desea continuar Si/No: ").lower()
    if continuar == "No".lower() and "N".lower():
        print("Fin del programa.")
        break
    else:
        continue