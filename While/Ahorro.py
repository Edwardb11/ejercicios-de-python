#Realizar un algoritmo para determinar cuánto ahorrará una persona en un año, si al final de cada mes deposita cantidades variables de dinero; además, se quiere saber cuánto lleva ahorrado cada mes.

cant_mensual = int(input())
mes =0
ahorro=0
while mes <=12:
    print("¿Cuánto has ahorrado en el mes ",mes,"?")
    cant_mensual = int(input())
    ahorro = ahorro + cant_mensual
    mes = mes +1
print(f"En el mes {mes} llevas ahorrado {ahorro}")

