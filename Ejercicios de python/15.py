#15. Hacer una función cdig(n, d), se desea que dicha función retorne las veces que el dígito d está contenido en el número n. Por ejemplo: 
#cdig(1241, 1) = 2.
#cdig(28858, 8)=3.

def cdig(n,d):
    a = n.count(d)
    return a
print(cdig("1122","1")) 
print(cdig("28858", "8")) #4
