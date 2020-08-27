#Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó RD$10, el segundo RD$20, el tercero RD$40 y así sucesivamente. Realizar un algoritmo para determinar cuánto debe pagar mensualmente y el total de lo que pagó después de los 20 meses.

primer_mes = 10
cont =0
while cont <=20:
    print(f"En el mes {cont} pago {primer_mes}")
    primer_mes = primer_mes*2
    cont= cont+1
    
print(f"EL pago total es {primer_mes}")
