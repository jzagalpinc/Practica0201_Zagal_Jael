# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.

# Pide al usuario la inversión inicial y la convierte a decimal.
inversion = float(input("Ingrese la inversión realizada\n"))  
# Establece un interés fijo del 4%.
interes = 0.04  
# Calcula el balance después del primer año.
balance1 = round(inversion * (1 + interes), 2)  
# Calcula el balance después del segundo año.
balance2 = round(balance1 * (1 + interes), 2)  
# Calcula el balance después del tercer año.
balance3 = round(balance2 * (1 + interes), 2)  
# Muestra el balance de cada año.
print(f"El balance del primer año es de : {balance1}€")  
print(f"El balance del segundo año es de : {balance2}€")  
print(f"El balance del tercer año es de : {balance3}€")  
