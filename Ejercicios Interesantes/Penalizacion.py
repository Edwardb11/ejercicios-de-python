#3)Un corredor, en una competencia de 400 metros con obstáculos realiza la siguiente presentación: los primeros 100
#  metros los corre en 4.5 segundos, los próximos 200 metros los recorre en 12 segundos y los últimos 100 los 
# recorre en 8.3 segundos. Los árbitros se dan cuenta que salió 1 segundo antes de sonar el disparo de inicio de la
#carrera por lo que lo penalizan con 2 segundos. También notan que al saltar 2 de los 6 obstáculos los rozó por 
#lo que le penalizan con otros 2.5 segundos por obstáculos tocados. Calcular y mostrar cuánto tiempo le tomó al 
# corredor recorrer los 400 metros.

P100M = 4.5
S200M = 12
T100M = 8.3

Total_Tiempo = P100M + S200M + T100M

Penalizacion_Salida = 2
Penalizacion_Obstaculos = 2.5

Total_Tiempo_Penalizacion = Penalizacion_Salida + (Penalizacion_Obstaculos * 2)

print('Tiempo que tomo recorrer los 400 metros: ' + str(Total_Tiempo) +
   '\n' 'Tiempo despues de calcular las penalizaciones: ' + str(Total_Tiempo + Total_Tiempo_Penalizacion))


