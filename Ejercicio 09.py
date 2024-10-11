# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

# Pide al usuario la cantidad que quiere invertir y la convierte a decimal.
cantidad_invertir = float(input("Escriba la cantidad a invertir\n"))  
# Pide al usuario el interés anual y lo convierte a decimal.
interes_anual = float(input("Ingrese el interés anual\n"))  
# Pide al usuario el número de años y lo convierte a entero.
numero_años = int(input("Ingrese el número de años\n"))  
# Calcula el capital que se obtendrá al final de la inversión.
capital = round(cantidad_invertir * (1 + interes_anual / 100) ** numero_años, 2)  
# Muestra el capital que se obtendrá.
print(f"El capital obtenido por la inversión es de {capital}")  
