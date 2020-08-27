def string1 (letra,indice1, indice2):
    if indice1 >= 0 and indice2 < len(letra) and indice1 < indice2:
        return letra[indice1:indice2]
    else:
        print("Vuelva a intentarlo, indices fuera de rango.")
letra = input("Ingrese su texto:" )
indice1 = int("Ingrese el indice:" )
indice2 = int("Ingrese el indice:" )
print(string1(letra,indice1,indice2))