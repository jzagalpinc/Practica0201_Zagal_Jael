# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.
peso = float(input("Ingrese su peso en kilogramos\n"))
altura = float(input("Ingrese su altura en metros\n"))
imc = round(peso / altura ** 2,2)
print(f"Tu índice de masa de corpotal es {imc}")
