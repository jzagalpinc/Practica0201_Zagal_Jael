#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.0
payasos = int(input("Introducir el número de payasos a enviar\n"))
muñecas = int(input("Introducir el número de muñecas a enviar\n"))
peso_payasos = payasos * 112
peso_muñecas = muñecas * 75
print(f"El peso total del paquete de payasos es igual a {peso_payasos}g y el de
      muñecas es {peso_muñecas}g")
