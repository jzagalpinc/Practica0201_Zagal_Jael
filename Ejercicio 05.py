#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

# Pide al usuario la paga por hora y la convierte a un número decimal.
precio_hora = float(input("Introduce la paga por hora por favor \n"))  
# Pide el número de horas trabajadas y lo convierte a decimal.
horas_trabajadas = float(input("Introduce el número de horas trabajadas \n"))  
# Calcula la paga total y redondea el resultado a dos decimales.
paga = round(precio_hora * horas_trabajadas, 2)  
# Muestra la paga total calculada.
print(f"Tu paga correspondiente es de {paga}")


