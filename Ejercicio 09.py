# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.
cantidad_invertir = float(input("Escriba la cantidad a invertir\n"))
interes_anual = float(input("Ingrese el interés anual\n"))
numero_años = int(input("Ingrese el número de años\n"))
capital = round(cantidad_invertir * (1 + interes_anual / 100) ** numero_años,2)
print(f"El capital obtenido por la inversión es de {capital}")