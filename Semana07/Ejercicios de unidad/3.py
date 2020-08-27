##El programa debe preguntar el artículo y su precio y añadir el par al diccionario,
  #hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista 
  #de la compra y el coste total, con el siguiente formato
#Lista de la compra
#Artículo 1      Precio
#Artículo 2     Precio
#Artículo 3      Precio
#------------------------------------
#Total              Coste

Diccionario = {}
more = 'Si'
while more == 'Si':
    articulos = input('Introduce un artículo: ')
    precio = float(input(f'Introduce el precio de {articulos}: '))
    Diccionario[articulos] = precio
    more = input('¿Quieres añadir artículos a la lista (Si/No)? ')
cost = 0
print('Lista de la compra')
for articulos, precio in Diccionario.items():
    print(articulos, '\t', precio)
    cost += precio
print('Coste total: ', cost)