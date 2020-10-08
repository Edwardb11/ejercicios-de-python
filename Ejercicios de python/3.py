#Haga un programa el cual solicite una longitud expresada en pulgadas e imprima la misma 
# longitud en yardas, pies y pulgadas. 
# Por ejemplo, una longitud de 65 pulgadas sería expresada como 1 yarda, 2 pies y 5 pulgadas.

x =  int(input("Ingrese una logitud: ")); 

pie =  x * 1.0 / 12 
yarda =  x * 1.0  / 36
pulgadas = x * 1 / 2.54


print(f"La longitud que usted ingreso fue:\n {x} {pie} \n pie   {yarda} yarda \n {pulgadas}  pulgadas" );