# ejercicio inicial
import time

lloviendo = input("Esta lloviendo? Y/N: ")

if lloviendo == 'Y':
    sombrilla = input("Tienes sombrilla? Y/N: ")
    if sombrilla == 'Y':
        print("Puedes salir")
    else:
        print("Espero un rato")
        time.sleep(5)
        lloviendo = input('Esta lloviendo? Y/N: ')
        if lloviendo == 'Y':
            print('Me quedo estudiando Python')
        else:
            print('Salgo afuera')
else:
    print('Salgo afuera')

print("Gracias por participar!!")
