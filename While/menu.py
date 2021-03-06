#Realizar un ejemplo de menú, donde podemos escoger las distintas opciones hasta que seleccionamos la opción de “Salir”.

opcion = int(input("Elija una opcion: "))
while True:
    if(opcion==1):
         print("Peliculas recomendables:")
         print(" + Los sietes pecados capitales (David Fincher )")
         print (" + Yo antes de ti (Thea Sharrock)")
         print (" + Milagros del Cielo (Patricia Riggen)")
         opcion = int(input("Elija una opcion: "))
    elif(opcion==2):
        print ("Series recomendables:")
        print ( " + La casa de papel (2019)")
        print ( " + Riverdale  (2017)")
        print ( " + Sabrina (2018)")
        opcion = int(input("Elija una opcion: "))
    elif(opcion==3):
        print ( "Novelas recomendables:")
        print (" + Amor de contrabando (2014)")
        print (" + La Reina del Sur (2011)")
        print (" + La Reina del Flow (2018)")
        opcion = int(input("Elija una opcion: "))
    elif(opcion==4):
         print ( "Videojuegos recomendables")
         print (" + Fornite (2017)")
         print (" + Grand Theft Auto V (2013)")
         print (" + Minecraft (2009)")
         opcion = int(input("Elija una opcion: "))
    elif(opcion==5):
          print ("Gracias, vuelva pronto")
          break
    else:
          print ("Opción no válida")
          opcion = int(input("Elija una opcion: "))
          