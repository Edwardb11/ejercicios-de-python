#Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla,
 #pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de
  #ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje
   #informando de ello.
#Fruta         Precio
#Plátano    1.35
#Manzana  0.80
#Pera           0.85
#Naranja     0.70
Almacen = {'Platano':1.35, 'Manzana':0.8, 'Pera':0.85, 'Naranja':0.7}
Fruta = input('¿Qué fruta quieres? ').title() #Escriba la primera letra en mayúscula de cada palabra
kg = float(input('¿Cuántos kilos? '))
if Fruta in Almacen:
    print(kg, 'kilos de', Fruta, 'valen', Almacen[Fruta]*kg )
else: 
    print(f"Lo siento, la fruta {Fruta} no está disponible.")