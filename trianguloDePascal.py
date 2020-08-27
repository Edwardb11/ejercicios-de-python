def factorial(n):
    proceso = 1
    for i in range(n):
        proceso *= i+1
    return proceso

def nckfactorial(n, k):
	return factorial(n) / (factorial(k) * factorial(n-k))

def nckmultiplicative(n, k):
	result = 1
	for i in range(1, k+1):
		result = result * (n-(k-i))/i
	return result

def pascal(n):
	lista= []
	ns = range(n)
	for n in ns:
		nlist = []
		for k in range(n+1):
			nlist.append(nckmultiplicative(n, k))
		lista.append(nlist)
	return lista
n= int(input("Numero de filas : "))
print(pascal(n))