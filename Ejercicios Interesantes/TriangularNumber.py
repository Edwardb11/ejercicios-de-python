# Question 2. Triangular Numbers

# The triangular numbers are the numbers 1, 3, 6, 10, 15, 21, ...
# They are calculated as follows.

# 1
# 1 + 2 = 3
# 1 + 2 + 3 = 6
# 1 + 2 + 3 + 4 = 10
# 1 + 2 + 3 + 4 + 5 = 15

# Write a procedure, triangular, that takes as its input a positive 
# integer n and returns the nth triangular number.
# Pregunta 2. Números triangulares

# Los números triangulares son los números 1, 3, 6, 10, 15, 21, ...
# Se calculan de la siguiente manera.


# Escriba un procedimiento, triangular, que tome como entrada un positivo
# entero ny devuelve el n-ésimo número triangular.
def triangular(n):
    if n ==1:
        return 1
    else:
        return n+triangular(n-1)
            
print (triangular(1))
#>>>1

print (triangular(3))
#>>> 6

print (triangular(10))
#>>> 55
