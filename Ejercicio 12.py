# Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y la ganancia final total.
# Pide al usuario cuántas barras de pan vendidas no son del día y las convierte a entero.

barras = int(input("Ingrese la cantidad de barras de pan vendidas que no son del día\n"))  
# Establece el precio normal de una barra de pan.
precio = 3.49  
# Establece el descuento que se aplicará al precio.
descuento = 0.6  
# Calcula el precio final aplicando el descuento y redondea a dos decimales.
precio_con_descuento = round(precio * barras * (1 - descuento), 2)  
# Muestra el precio común de las barras de pan.
print(f"El precio común de las barras de pan es de: {precio}")  
# Muestra el porcentaje de descuento aplicado.
print(f"El descuento por no ser fresca es de: {descuento * 100}%")  
# Muestra el precio final que debe pagar el usuario.
print(f"El precio final a pagar es: {precio_con_descuento}")  
