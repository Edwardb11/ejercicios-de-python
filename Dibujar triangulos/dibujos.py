def figuras():
    print("Figura 1")
    x=1
    while x<=10:
        espacio=10-x
        print(" "*espacio+"*"*x)
        x+=1

    print("Figura 2")
    x=10
    while x>=1:
        espacio=10-x
        print(" "*espacio+"*"*x)
        x-=1

    print("Figura 3")
    x=1
    while x<=10:
        espacio=10-x
        print(" "*espacio+"* "*x)
        x+=1
    
    print("Figura 4")
    x=10
    while x>=1:
        espacio=10-x
        print(" "*espacio+"* "*x)
        x-=1

figuras()