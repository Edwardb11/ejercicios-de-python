def dibujos1():
    print("Figura 1")
    for i in range(11):
        espacio=10-i
        print(" "*espacio+"*"*i)

    print("Figura 2")
    for i in range(10,0,-1):
        espacio=10-i
        print(" "*espacio+"*"*i)

    print("Figura 3")
    for i in range(11):
        espacio=10-i
        print(" "*espacio+"* "*i)

    print("Figura 4")
    for i in range(10,0,-1):
        espacio=10-i
        print(" "*espacio+"* "*i)
dibujos1()