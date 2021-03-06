import random
import time
import os

def seleccion():
    print()
    print("Inicia el simbolo O")
    print()
    print("Favor elegir: O / X")
    print()

    simbolo = ""
    while simbolo != "O" and simbolo != "X":
        simbolo = input("Favor introducir el simbolo del jugador uno: ").upper()

    if simbolo == "O":
        jugadorUno = "O"
        maquina = "X"
    else:
        jugadorUno = "X"
        maquina = "O"

    return jugadorUno, maquina

def tableros(tablero):
    print()
    print("1       |2       |3")
    print("   {}   |   {}   |   {}".format(tablero[0], tablero[1], tablero[2]))
    print("        |        |")
    print("--------+--------+--------")
    print("4       |5       |6")
    print("   {}   |   {}   |   {}".format(tablero[3], tablero[4], tablero[5]))
    print("        |        |")
    print("--------+--------+--------")
    print("7       |8       |9")
    print("   {}   |   {}   |   {}".format(tablero[6], tablero[7], tablero[7]))
    print("        |        |")
    print()

def otraVez():
    print()
    respuesta = input("¿Desea jugar otra vez? Si(S) / No(N)").upper()
    if respuesta == "S" or respuesta == "SI":
        return True
    else:
        return False

def ganador(tablero, jugador):
    if tablero[0] == tablero[1] == tablero[2] == jugador or \
        tablero[3] == tablero[4] == tablero[5] == jugador or \
        tablero[6] == tablero[7] == tablero[8] == jugador or \
        tablero[0] == tablero[3] == tablero[6] == jugador or \
        tablero[1] == tablero[4] == tablero[7] == jugador or \
        tablero[2] == tablero[5] == tablero[8] == jugador or \
        tablero[0] == tablero[4] == tablero[8] == jugador or \
        tablero[2] == tablero[4] == tablero[6] == jugador:
        return True
    else:
        return False

def espacioLleno(tablero):
    
    for i in tablero:
        if i == " ":
            return False
    else:
        return True

def espacioLibre(tablero, casilla):

    return tablero[casilla] == " "

def movimiento(tablero):
    posiciones = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    posicion = None
    while True:
        if posicion not in posiciones:
            posicion = input("Selecione una casilla del 1-9: ")
        else:
            posicion = int(posicion)
            if not espacioLibre(tablero, posicion-1):
                print("Esta casilla esta ocupada, por favor intentarlo de nuevo con otra diferente")
            else:
                return posicion-1

def maquinaFacil(tablero, jugador):
    for i in range(9):
        copia = list(tablero)
        if espacioLibre(copia, i):
            copia[i] = jugador
            if ganador(copia, jugador):
                return i

    while True:
        casilla = random.randint(0,8)
        if not espacioLibre(tablero, casilla):
            casilla = random.randint(0,8)
        else:
            return casilla

#******Programa pricipal******#
jugando= True
while jugando:
    tablero = [" "] * 9
    os.system("cls")
    os.system("cls")
    jugadorUno, maquina = seleccion()
    os.system("cls")
    tableros(tablero)

    if jugadorUno == "O":
        turno = "jugadorUno"
    else:
        turno = "maquina"

    partida = True
    while partida:
        if espacioLleno(tablero):
            print("Empate")
            partida = False

        elif turno == "jugadorUno":
            casilla = movimiento(tablero) 
            tablero[casilla] = jugadorUno
            turno = "maquina"
            os.system("cls")
            tableros(tablero)
            if ganador(tablero, jugadorUno):
                print("Jugador Uno ha ganado")
                partida = False

        elif turno == "maquina":
            print("Por favor espere mientras la maquina calcula el siguiente movimiento")
            time.sleep(2)
            casilla = maquinaFacil(tablero, jugadorUno)
            turno = "jugadorUno"
            os.system("cls")
            tableros(tablero)
            if ganador(tablero, maquina):
                print("Jugador uno ha perdido")
                partida = False

    jugando = otraVez()