# ordenar los valores de una lista
import os
os.system("cls")
 
def listaOrganizar(lista):
    for i in range(1,len(lista)):
        elemento = lista[i]
        indice = i
        # print(lista[i])
 
        while indice > 0 and lista[indice - 1] > elemento:            
            lista[indice] = lista[indice - 1]
            indice = indice - 1
 
        lista[indice] = elemento
 
lista = [2000, 300, 25, 40, 31, 19, 50, 45]
print(f"Valores desorganizados : {lista}")
listaOrganizar(lista)
 
print(f"Valores organizada : {lista}")
