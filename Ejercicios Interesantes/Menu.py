import random
from colorama import Fore, Back,Style,init
init()
#funcion de acceso al sistema
def adm(intentos=1):
    print ("Intento #: ", intentos)
    usuario= input("Nombre de usuario: ").lower()
    clave= input("Digite su contraseña: ").lower()
    
    if usuario!= "admin" and clave != "admin":
        if intentos<3:
            intentos += 1 
            print(f"Nombre de usuario o contraseña incorrecto!, intentalo otra vez")
            adm(intentos)
        else:
            print("Has agotado todos los intentos.")
            
    if usuario== "admin" and clave == "admin":
        print ("Usuario válido. Bienvenido al sistema!\n \n")
        return opciones()

#Menu de opciones
def opciones():
    print("*******************************************************************************************************")
    print("***    UNIVERSIDAD CATOLICA DEL CIBAO            Matricula:     2019-0823                           ***")
    print("***    UCATECI                                                  Nombre:      Edward Brito Diaz      ***")
    print("***    PROGRAMACION 1                                                                               ***")
    print("***    MENU PRINCIPAL                                                                               ***")
    print("*******************************************************************************************************")

    print("\nBienvenido al Menu Principal\n")
    print("\n1)Calcula tiempo \n2)Calcula Calificación \n3)Mi función \n4)Generador de series \n5)Figuras \n0)Salir")
    opcion = int(input("Elija una opcion: "))
    while True:
        if(opcion==1):
             edad()
        elif(opcion==2):
            calificacion()
        elif(opcion==3):
            miFuncion()
        elif(opcion==4):
            serie()
        elif(opcion==5):
            bandera()
        elif(opcion==0):
             print ("Gracias, vuelva pronto")
             break
        else:
             print ("Opción no válida")
             opcion = int(input("Elija una opcion: "))
#opcion1
def edad():
    edad= int(input("Ingrese su edad: "))
    mes=edad*12
    semanas=edad*52
    dias=edad*365
    horas= edad*8760
    minutos= edad*525600
    segundos= edad*31536000
    print(f"La persona ha vivido:\n{mes} Meses \n{semanas} Semanas \n{dias} Dias \n{horas} Horas \n{minutos} Minutos \n{segundos} Segundos")
    return opciones()


#Opcion #2
def calificacion():
            #Si introduzco -1 debo retornar al menu de opciones
    print("Elegiste Calcular la calificion.")

    Suma1=0
    Suma2=0
    Suma3=0
    Suma4=0
    Suma5=0
    while True:
        TI=int(input("Ingrese su nota de trabajo de investigacion: "))
        if TI==-1:
            return opciones()
        if TI>=0 and TI<=15:
            Suma1+=TI
            break
        else:
            print("El valor introducido esta fuera del rango solicitado.")

    while True:
        TP=int(input("Ingrese su nota de trabajo practico: "))
        if TP==-1:
            return opciones()
        if TP>=0 and TP <=25:
            Suma2+=TP
            break
        else:
            print("El valor introducido esta fuera del rango solicitado.")

    while True:
        PP=int(input("Ingrese su nota del primer parcial: "))
        if PP==-1:
            return opciones()
        if PP>=0 and PP <=20:
            Suma3+=PP
            break
        else:
            print("El valor introducido esta fuera del rango solicitado.")

    while True:
        SP=int(input("Ingrese su nota del segundo parcial: "))
        if SP==-1:
            return opciones()
        if SP>=0 and SP<=15:
            Suma4+=SP
            break
        else:
            print("El valor introducido esta fuera del rango solicitado.")

    while True:
        EF=int(input("Ingrese su nota del examen final: "))
        if EF==-1:
            return opciones()
        if EF>=0 and EF<=25:
            Suma5+=EF
            break
        else:
            print("El valor introducido esta fuera del rango solicitado.")    


        #Sumando el rango de calificaciones
    suma=Suma1 + Suma2 + Suma3 + Suma4 + Suma5

        #Comparando calificacion final
    if suma>=90 and suma<=100:
        print("Tu calificacion final es: A")
    elif suma>=80 and suma<=89:
        print("Tu calificacion final es: B")
    elif suma>=70 and suma <=79:
             print("Tu calificacion final es: C")
    elif suma>=60 and suma<=69:
        print("Tu calificacion final es: D")
    else:
        print("Tu calificacion final es: F")
    return opciones()

#opcion3
#Crear una funcion a mi gusto
# tener 6 oportunidades para encontrar respuesta
def miFuncion():
    print("\n Programa de generar numeros aletarios, tienes 6 intentos para adivinar\n")
    numeroSecreto = random.randint(1, 20)
    print("Piensa en un numero entre 1 al 20")
    for numeroIntentos in range(1,7):
        respuesta = int(input("Ingresa una opcion: "))

        if respuesta < numeroSecreto:
            print("El valor ingresado esta por debajo del numero")
        elif respuesta > numeroSecreto:
            print("El valor ingresado esta por encima del numero")
        else:
            break

    if respuesta == numeroSecreto:
        print(f"Buen trabajo has adivinado en {numeroIntentos} intento, felicidades!!")
    else:
        print(f"A sobrepasado el numero de intentos, el numero secreto era {numeroSecreto}")

    return opciones()


#Opcion 4


def serie():
    #Usando lista
    print("\nSerie 1")
    Serie1= int(input("Ingrese la serie de numeros: "))
    lista=[]
    for j in range(1,Serie1+1):
        lista.append(j)
    print(lista)
    for e in lista:
        lista.pop()
        print(lista)
    lista.pop()
    print(lista)

    #Usando la forma del profe
    for x in range(Serie1,0,-1):
        s=""
        for y in range(1,x+1):
            s+= str(y)+""
        print(s) 

    #Usando lista
    print("\nSerie 2")
    lista1=[]
    for i in range(Serie1,0,-1):
        lista1.append(i)
        print(lista1)
    return opciones()


def bandera():
    print("Bandera de Venezuela")
    n=60
    for i in range(1,10):
        if i>1 and i<=4:
            print(Fore.YELLOW+Back.YELLOW+n*" ")
        if i>4 and i<=7:
            print(Fore.BLACK+Back.BLUE+n*" ")
        elif i>7 and i<=10:
            print(Fore.RED+Back.RED+n*" ") 
    print(Fore.WHITE+Back.BLACK)
    return opciones()
print(adm())