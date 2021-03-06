#Realizar un programa que rellene una lista con 10 números enteros consecutivos y haga una copia de esa lista en otra.

Lista =[]
for a in range (1,11,1):
    Lista.append(a)
Lista2= [Lista]
print(Lista[:])
print(Lista2[:])

    