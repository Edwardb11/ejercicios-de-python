# Bola Magica
import random

def evaluarRespuestas(respuesta):
    if respuesta == 1:
        return("Es cierto")
    elif respuesta == 2:
        return("Es decididamente que si")
    elif respuesta == 3:
        return("Sí definitivamente")
    elif respuesta == 4:
        return("Respuesta confusa, intenta otra vez")
    elif respuesta == 5:
        return("Pregunta de nuevo más tarde")
    elif respuesta == 6:
        return("Concentrate y pregunta luego")
    elif respuesta == 7:
        return("Mi respuesta es que no")
    elif respuesta == 8:
        return("Las opciones no son tan buenas")    
    else:
        return("Muy dudoso")    


pregunta = input("Realiza una pregunta: ")
r = random.randint(1,9)
posibleRespuesta = evaluarRespuestas(r)
print(posibleRespuesta)
