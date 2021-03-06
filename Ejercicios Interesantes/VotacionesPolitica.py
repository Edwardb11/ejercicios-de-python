print("Programa para ejercer su voto")
Recibido= 0
Nulo=0
votar= int(input("Cuantas votaciones va hacer: "))
x=0
PRM=0
PLD=0
PRSC=0
while votar >=x:
    edad= int(input("Ingresa la edad: "))
    if edad >=18:
        while True:
            voto=int(input("Votaras por 1 PLD, 2 PRM, 3 PRSC: "))
            if voto== 1:
                PLD+=1
                break
            elif voto ==2:
                PRM+=1
                break
            elif voto ==3:
                PRSC+=1
                break
            else:
                print("Fuera de rango. ")
        Recibido+=1
    else:
        Nulo+=1
    x+=1
if PLD>PRM:    
    votoMAX="PLD"
elif PRM>PRSC:
    votoMAX="PRM"
elif PRSC>PLD :
    votoMAX="PRSC"
else:
    votoMAX="Empate"
print(f"El partido PRM genero:{PRM} votos \nEl partido PLD genero:{PLD} votos \nEl partido PRSC genero:{PRSC}")
print(f"El partido que mas voto obtuvo fue:{votoMAX}" )
print(f"La cantidad de votos validos es: {Recibido} y nulos: {Nulo}")
