# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.

# Pide al usuario su peso en kilogramos y lo convierte a decimal.
peso = float(input("Ingrese su peso en kilogramos\n"))  
# Pide al usuario su altura en metros y la convierte a decimal.
altura = float(input("Ingrese su altura en metros\n"))  
# Calcula el índice de masa corporal (IMC) y lo redondea a dos decimales.
imc = round(peso / altura ** 2, 2)  
# Muestra el IMC calculado.
print(f"Tu índice de masa de corporal es {imc}")  
