# 2)      Un agente de cambio necesita un programa que le permite saber cuánto debe entregar 
# a sus clientes de acuerdo a la tasa de cambio actual. Sabiendo que la tasa de cambio 
# del dólar es: US$ 1 x RD$ 57, la del euro es:  EU$ 1 x RD$ 63 y la del Yuan chino: CNY$ 1 x RD$ 7.7; 
# se le pide que al introducir cuantos pesos dominicanos se tiene, 
# calcule y muestre a cuanto equivale cambiándolo a las monedas indicadas.

def cambio():
    cambiar=float(input("Digite la cantidad de pesos dominicanos: "))
    print("Digite a que quiere cambiar:\nDólar:US$ \nEuro:EU$ \nYuan chino:CNY$  ")
    eleccion= input("Digite su eleccion: ").upper()
    dolar=cambiar*57
    euro=cambiar*63
    yuan=cambiar*7.7
    if eleccion=="DOLAR" or "US":
        print(f"{cambiar} pesos equivalen a {dolar} dolares")
    elif eleccion =="EURO" or "EU":
        print(f"{cambiar} pesos equivalen a {euro} euro")
    elif eleccion=="YUAN CHINO" or "CNY":
        print(f"{cambiar} pesos equivalen a {yuan} yuan")

cambio()
    