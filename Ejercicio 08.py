#Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.

# Pide al usuario el primer número entero y lo convierte a entero.
n = int(input("Ingrese su primer número entero\n"))  
# Pide al usuario el segundo número entero y lo convierte a entero.
m = int(input("ingrese su segundo número entero\n"))  
# Calcula el cociente de n entre m.
c = n / m  
# Calcula el resto de n dividido entre m.
r = n % m  
# Muestra el cociente y el resto.
print(f"El cociente del primer número sobre el segundo es igual {c} y su resto es igual a {r}")  
