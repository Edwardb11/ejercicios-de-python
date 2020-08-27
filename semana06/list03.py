# trabajando con listas

# imprimiendo elementos de una lista con ciclo for
utiles = ["Lapicero", "Lapiz", "Mochila", "Cuaderno"]
for i in range(len(utiles)):
    print(f"El indice {i} posee el articulo {utiles[i]}")

# buscar elementos en una lista
buscar = input("Ingresa el articulo a buscar: ")

if buscar in utiles:
    print(f"El articulo {buscar} se encuentra en la lista")
else:
    print(f"El articulo {buscar} no se encuentra en la lista")

