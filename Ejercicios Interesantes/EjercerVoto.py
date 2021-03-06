print("Programa para ejercer su voto")
Recibido= 0
Nulo=0
votar= int(input("Cuantas votaciones va hacer: "))
x=0
PRM=0
PLD=0
while votar >=x:
    edad= int(input("Ingresa la edad: "))
    if edad >=18:
        while True:
            voto=int(input("Votaras por 1 PLD, 2 PRM: "))
            if voto== 1:
                PLD+=1
                break
            else:
                PRM+=1
                break
        Recibido+=1
    else:
        Nulo+=1
    x+=1
print(f"La cantidad de votos validos es: {Recibido} y nulos: {Nulo}")
