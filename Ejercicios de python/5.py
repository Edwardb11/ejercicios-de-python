#Los conejos de Fibonacci. El matemático Leonardo Fibonacci expuso el siguiente problema,
#  haga un programa para solucionarlo. Suponga que una pareja de conejos tiene un par 
# (una hembra y un macho) de crías cada mes y a la vez las crías se hacen fértiles al cabo de un mes. 
# Si comenzamos con una pareja fértil y no muere.  
# ¿Cuántos pares de conejos se tendrían al cabo de un año?

n=365
a, b = 0,1
while a < n:
     print(a, end=' ')
     a, b = b, a + b

