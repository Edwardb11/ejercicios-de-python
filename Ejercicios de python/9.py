#Usando Ciclos, escriba un programa que imprima por pantalla los siguientes gráficos. 
# (Pensar en una forma inteligente de hacerlo)
#a)
#******
#*****
#****
#***
#**
#*
print("Grafico a")
for i in range(1, 6+1):
    for j in range(7- i):
        print("* ", end="")
    print()


#b)
#*
#***
#*****
#*******
#*********
print("Grafico b")
for i in range(1, 9 + 1):
    for j in range(i):
        print("* ", end="")
    print()

#c) 
#*
#***
#*****
#*******
#*********
#*******
#*****
#***
#*

print("Grafico c")
for i in range(1, 6 + 1):
    for j in range(i):
        print("* ", end="")
    print()

for i in range(1, 6):
    for j in range(6- i):
        print("* ", end="")
    print()