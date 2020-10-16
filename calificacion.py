def calificacion():
    nombre= input("Introduce tu nombre:").capitalize()
    matricula=int(input("Introduce tu matricula:"))
    print(f"Se registro el nombre de usuario de {nombre } portador de la matricula {matricula}")
    Suma1=0 
    Suma2=0 
    Suma3=0 
    Suma4=0
    while True:
        TI=int(input("Ingrese su nota de trabajo de investigacion: "))
        if TI>=0 and TI<=100:
            Suma1+=TI
            break
        else:
            print("El valor introducido esta fuera del rango solicitado.")
    while True:
        PP=int(input("Ingrese su nota del primer parcial: "))
        if PP>=0 and PP <=100:
            Suma2+=PP
            break
        else:
            print("El valor introducido esta fuera del rango solicitado.")
    while True:
        SP=int(input("Ingrese su nota del segundo parcial: "))
        if SP>=0 and SP<=100:
            Suma3+=SP
            break
        else:
            print("El valor introducido esta fuera del rango solicitado.")
    while True:
        EF=int(input("Ingrese su nota del examen final: "))
        if EF>=0 and EF<=100:
            Suma4+=EF
            break
        else:
            print("El valor introducido esta fuera del rango solicitado.")    

    suma=(Suma1 + Suma2 + Suma3 + Suma4)/4
    print(f"La calificacion final de {nombre} es: {suma}")

    #if suma>=90 and suma<=100:
     #   print(f"La calificacion final de {nombre} es: A")
    #elif suma>=80 and suma<=89:
     #  print(f"La calificacion final de {nombre} es: B")
    #elif suma>=70 and suma <=79:
     #   print(f"Tu calificacion final {nombre} es: C")
    #elif suma>=60 and suma<=69:
     #   print(f"La calificacion final de {nombre} es: D")
    #else:
    #   print(f"La calificacion final de {nombre} es: F")
        #break
print(calificacion())


