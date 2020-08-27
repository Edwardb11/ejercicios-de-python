
#Valores= [2,4,6,8,10]
#Valores[3] = "hola"

#print(Valores)

#valores = ['a', 'b', 'c', 'd']
#print(valores[:2])

valores = [3.14, 'gato', 11, 'gato', 'verdadero']
valores.remove('gato')
print(valores)

utiles= ["Lapicero", "Lapiz", "Mochila", "Cuaderno"]
for i in range(len(utiles)):
    print(f"El indice {i} posee el articulo {utiles[i]}")


buscar= input("Ingresa el articulo a buscar: ")

if buscar in utiles:
    print(f"El articulo {buscar} se encuentra en la lista")
else:
    print(f"El articulo {buscar} no se encuentra en la lista")
