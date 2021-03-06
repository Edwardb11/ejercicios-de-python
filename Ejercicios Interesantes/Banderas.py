from colorama import Fore, Back,Style,init
init()
def bandera():
    print("Bandera de Venezuela")
    n=60
    for i in range(1,10):
        if i>1 and i<=4:
            print(Fore.YELLOW+Back.YELLOW+n*" ")
        if i>4 and i<=7:
            print(Fore.BLACK+Back.BLUE+n*" ")
        elif i>7 and i<=10:
            print(Fore.RED+Back.RED+n*" ") 
    print(Fore.WHITE+Back.BLACK)

bandera()