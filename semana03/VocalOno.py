#Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ en caso contrario, el programa termina cuando se introduce un espacio.

caracteres = input("Introduce caracteres: ").lower()
while caracteres != " ":
    if caracteres == "a" and "e" and "i" and "o" and "u" :
       print(f"Has introducido la vocal {caracteres}")
    else: 
        print("No has introducido Una Vocal")
    caracteres= input("Introduce caracteres: ")
