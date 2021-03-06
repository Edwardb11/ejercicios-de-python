
Clase= int(input("Ingrese la calificacion de la clase: "))
Tareas= int(input("Ingrese la calificacion de las tareas: "))
Proyectofinal= int(input("Ingrese la calificacion del proyecto: "))
Examenfinal= int(input("Ingrese la calificacion del examen: "))

Suma= Clase + Tareas + Proyectofinal + Examenfinal

if Clase<=35 and Clase >0:
    print(f"su calificacion es {Suma}")
elif Tareas<=25 and Tareas >0:
    print(f"su calificacion es {Suma}")
elif Proyectofinal<=20 and Proyectofinal >0:
    print(f"su calificacion es {Suma}")
elif Examenfinal<=20 and Examenfinal >0:
    print(f"su calificacion es {Suma} ")
else:
    print("Valor ingresado incorrecto")


