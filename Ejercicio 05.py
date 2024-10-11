#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
precio_hora = float(input("Introduce la paga por hora por favor \n"))
horas_trabajadas = float(input("Introduce el número de horas trabajadas \n"))
paga = round(precio_hora * horas_trabajadas,2)
print(f"Tu paga correspondiente es de {paga}")



