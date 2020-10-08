#Haga una función que utilice números float, la ecuación debe resolver ecuaciones 
# cuadráticas con la forma ax^2+bx+c=0, ecuCuad(a, b, c) debe retornar la solución positiva de la ecuación 
# cuyo parámetros sean a, b y c respectivamente.

a = float(input('Ingrese a: '))
b = float(input('Ingrese b: '))
c = float(input('Ingrese c: '))

discriminante = b ** 2 - 4 * a * c
if discriminante < 0:
    print ('La ecuacion no tiene soluciones reales')
elif discriminante == 0:
    x = -b / (2 * a)
    print ('La solucion unica es x =', x)
else:
    x1 = (-b - (discriminante ** 0.5)) / (2 * a)
    x2 = (-b + (discriminante ** 0.5)) / (2 * a)
    print ('Las dos soluciones reales son:')
    print ('x1 =', x1)
    print ('x2 =', x2)
