from datetime import datetime
import os
usuario = "admin"
contraseña = 'admin'

def iniciar_sesion(intentos=1):  

    resp_usuario = input("Ingresa el nombre del Usuario >>> ") 
    resp_contraseña = input("Ingresa la contraseñ del Usuario >>> ") 

    if (resp_usuario != usuario and resp_contraseña != contraseña):   
        if intentos < 3: 
            intentos += 1 
            print ("Respuesta incorrecta!!! \n La contraseña y usuario no coinciden. \n Intentalo otra vez. Intentos # ", intentos) 
            iniciar_sesion(intentos)
            
        else: 
   
            print ("Ya no tiene intentos disponible. Bloqueando la cuenta...")

    else:
        opciones()
def texto_centralizado ():
        titulo1 = ('UNIVERSIDAD CATÓLICA DEL CIBAO')
        x1 = titulo1.center(60)
        
        titulo2 = ('UCATECI')
        x2 = titulo2.center(60)

        titulo3 = ('LABORATORIO DE PROGRAMACIÓN 1')
        x3 = titulo3.center(60)

        titulo4 = ('SEGUNDO PARCIAL')
        x4 = titulo4.center(60)

        titulo5 = ('NOMBRE DEL PROGRAMA')
        x5 = titulo5.center(60)

        now = datetime.today().strftime('%Y-%m-%d')

        print("********************************************************************")
        print(f"*** {x1} ***")
        print(f"*** {x2} ***")
        print(f"*** {x3} ***")
        print(f"*** {x4} ***")
        print(f"*** {x5} ***") 
        print(f"*** {now}                                                   ***" )
        print("********************************************************************")
def opciones():
    os.system ("cls")
    texto_centralizado()
    print("\nBienvenido al Menu Principal")
    print("\n1)Elegir Lab \n0)Salir")
    opcion = int(input("Elige una opcion: "))
    while True:
        if(opcion==1):
             select_lab()
        elif(opcion==0):
             print ("Gracias, vuelva pronto")
             break
        else:
             print ("Opción no válida")
             opcion = int(input("Elige una opcion: "))

def dias():
    #diseño de los dias
    os.system ("cls")
    f1=  ('---------------------')
    menu=('|       Dias        |')
    f2=  ('|-------------------|')
    op1= ('|   1- Lunes        |')
    op2= ('|   2- Martes       |')
    op3= ('|   3- Miercoles    |')
    op4= ('|   4- Jueves       |')
    op5= ('|   5- Viernes      |')
    op6= ('|   6- Sabado       |')
    op0= ('|   0- Salir        |')
    f3=  (' --------------------\n')
    #lleval los dias al centro
    a1 = f1.center(60)
    a2 = menu.center(60)
    a3 = f2.center(60)
    a4 = op1.center(60)
    a5 = op2.center(60)
    a6 = op3.center(60)
    a7 = op4.center(60)
    a8 = op5.center(60)
    a9 = op6.center(60)
    a10 = op0.center(60)
    a11 = f3.center(60)
    #imprimir los dias en el centro
    print()
    print(a1)
    print(a2)
    print(a3)
    print(a4)
    print(a5)
    print(a6)
    print(a7)
    print(a8)
    print(a9)
    print(a10) 
    print(a11)

def horas():
    os.system ("cls")
    #diseño de las horas
    f1=   ('------------------------------')
    menu= ('|           Horas            |')
    f2=   ('|----------------------------|')
    op1=  ('|   1- 8:00AM - 9:00AM       |')
    op2=  ('|   2- 9:00AM - 10:00AM      |')
    op3=  ('|   3- 10:00AM – 11:00AM     |')
    op4=  ('|   4- 11:00AM – 12:00PM     |')
    op5=  ('|   5- 12:00PM – 1:00PM      |')
    op6=  ('|   6- 1:00PM – 2:00PM       |')
    op7=  ('|   7- 2:00PM – 3:00PM       |')
    op8=  ('|   8- 3:00PM – 4:00PM       |')
    op9=  ('|   9- 4:00PM – 5:00PM       |')
    op10= ('|   10- 5:00PM – 6:00PM      |')
    op0=  ('|   0- Salir                 |')
    f3=   (' --------------------\n')
    #lleval las horas al centro
    a1 = f1.center(60)
    a2 = menu.center(60)
    a3 = f2.center(60)
    a4 = op1.center(60)
    a5 = op2.center(60)
    a6 = op3.center(60)
    a7 = op4.center(60)
    a8 = op5.center(60)
    a9 = op6.center(60)
    a10 = op7.center(60)
    a11 = op8.center(60)
    a12 = op9.center(60)
    a13 = op10.center(60)
    a14 = op0.center(60)
    a15 = f3.center(60)
    #imprimir las horas en el centro
    print()
    print(a1)
    print(a2)
    print(a3)
    print(a4)
    print(a5)
    print(a6)
    print(a7)
    print(a8)
    print(a9)
    print(a10) 
    print(a11)
    print(a12)
    print(a13)
    print(a14)
    print(a15)

def select_lab():
    os.system ("cls")
    print("Opciones  \n-a)  \n-b)  \n-c) \n-Menu)" )
    laboratorio=input('ingrese un laboratorio >>> ').lower()
    if laboratorio == 'a':
        dias()
        dia_selec=input('Selecciona un dia >>> ').lower()
        if dia_selec == 'lunes' :
            print('Nota: Para seleccionar una hora dijite el numero que esta al lado')
            horas()
            
            hora_selec=input('Selccione el horario que desea utilizar >>> ')
            if hora_selec == '1':
                print('El laboratorio esta ocupado')

        if dia_selec == 'martes':
            print('Nota: Para seleccionar una hora dijite el numero que esta al lado')
            horas()
        if dia_selec == 'miercoles':
            print('Nota: Para seleccionar una hora dijite el numero que esta al lado')
            horas()
        if dia_selec == 'jueves':
            print('Nota: Para seleccionar una hora dijite el numero que esta al lado')
            horas()
        if dia_selec == 'viernes':
            print('Nota: Para seleccionar una hora dijite el numero que esta al lado')
            horas()
        if dia_selec == 'sabado':
            print('Nota: Para seleccionar una hora dijite el numero que esta al lado')
            horas()
        else:
            opciones()

    if laboratorio == 'b':
        dias()

        dia_selec=input('Selecciona un dia >>> ').lower()
        if dia_selec ==  'lunes':
            print('Nota: Para seleccionar una hora dijite el numero que esta al lado')
            horas()
        if dia_selec ==  'martes':
            print('Nota: Para seleccionar una hora dijite el numero que esta al lado')
            horas()
        if dia_selec == 'miercoles':
            print('Nota: Para seleccionar una hora dijite el numero que esta al lado')
            horas()
        if dia_selec ==  'jueves':
            print('Nota: Para seleccionar una hora dijite el numero que esta al lado')
            horas()
        if dia_selec ==  'viernes':
            print('Nota: Para seleccionar una hora dijite el numero que esta al lado')
            horas()
        if dia_selec == 'sabado':
            print('Nota: Para seleccionar una hora dijite el numero que esta al lado')
            horas()
        else:
            opciones()

    if laboratorio  == 'c':
        dias()

        dia_selec=input('Selecciona un dia >>> ').lower()
        if dia_selec =='lunes':
            print('Nota: Para seleccionar una hora dijite el numero que esta al lado')
            horas()
        if dia_selec ==  'martes':
            print('Nota: Para seleccionar una hora dijite el numero que esta al lado')
            horas()
        if dia_selec ==  'miercoles':
            print('Nota: Para seleccionar una hora dijite el numero que esta al lado')
            horas()
        if dia_selec == 'jueves':
            print('Nota: Para seleccionar una hora dijite el numero que esta al lado')
            horas()
        if dia_selec == 'viernes':
            print('Nota: Para seleccionar una hora dijite el numero que esta al lado')
            horas()
        if dia_selec == 'sabado':
            print('Nota: Para seleccionar una hora dijite el numero que esta al lado')
            horas()
        else:
            opciones()
    
    else:
       os.system ("cls")
       opciones()
    

iniciar_sesion()
