Preguntar = input("Introduce una palabra: ")
logica= Preguntar
word = list(Preguntar)
logica = list(logica)
logica.reverse()
if Preguntar == logica:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")

#Haz una función que reciba un string y dos índices. Se debe retornar el string que va entre 
#las posiciones indicadas por los índices. Si las posiciones no son validas se debe avisar.
def string1 (letra,indice1, indice2):
    if indice1 >= 0 and indice2 < len(letra) and indice1 < indice2:
        return letra[indice1:indice2]
    else:
        print("Vuelva a intentarlo, indices fuera de rango.")
letra = input("Ingrese su texto:" )
indice1 = int(input("Ingrese el indice:" ))
indice2 = int(input("Ingrese el indice:" ))
print(string1(letra,indice1,indice2))


#Queremos realizar un programa que regule la cantidad de caracteres que se pueden
# escribir en una frase, siendo el limite de caracteres 60.
while True:
    frase= input("Introduce una frase: ")
    if len(frase) >60:
        print("Error")
    else:
        print(frase)

    continuar = input("Desea continuar Si/No: ").lower()
    if continuar == "No".lower() and "N".lower():
        print("Fin del programa.")
        break
    else:
        continue