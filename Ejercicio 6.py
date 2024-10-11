#Escribir un programa que lea un entero positivo, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n. La suma de los  primeros enteros positivos puede ser calculada de la siguiente forma: suma = (n (n + 1))/2
n = int(input("Introduce tu número entero \n"))     
suma = (n * (n + 1)) / 2
print(f"La suma de los primeros números enteros desde el 1 hasta el {n} es igual a {suma}")