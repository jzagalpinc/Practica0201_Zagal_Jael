#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.0

# Pide al usuario el número de payasos y lo convierte a entero.
payasos = int(input("Introducir el número de payasos a enviar\n"))  
# Pide al usuario el número de muñecas y lo convierte a entero.
muñecas = int(input("Introducir el número de muñecas a enviar\n"))  
# Calcula el peso total de los payasos.
peso_payasos = payasos * 112  
# Calcula el peso total de las muñecas.
peso_muñecas = muñecas * 75  
# Muestra el peso total de los payasos y de las muñecas.
print(f"El peso total del paquete de payasos es igual a {peso_payasos}g y el de muñecas es {peso_muñecas}g")  
