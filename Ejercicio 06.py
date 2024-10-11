#Escribir un programa que lea un entero positivo, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n. La suma de los  primeros enteros positivos puede ser calculada de la siguiente forma: suma = (n (n + 1))/2

# Pide al usuario un número entero y lo convierte a tipo entero.
n = int(input("Introduce tu número entero \n"))  
# Calcula la suma de todos los números del 1 hasta n.
suma = (n * (n + 1)) / 2  
# Muestra el resultado de la suma.
print(f"La suma de los primeros números enteros desde el 1 hasta el {n} es igual a {suma}")  
