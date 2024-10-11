# Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y la ganancia final total.
barras = int(input("Ingrese la cantidad de barras de pan vendidas que no son del día\n"))
precio = 3.49
descuento = 0.6
precio_con_descuento = round(precio * barras * (1 - descuento),2) 
print(f"El precio común de las barras de pan es de: {precio}")
print(f"El descuento por no ser fresca es de: {descuento * 100}%")
print(f"El precio final a pagar es: {precio_con_descuento}")