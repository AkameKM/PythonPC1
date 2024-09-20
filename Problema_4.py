"""
Escribir un programa que lea un entero positivo, N, introducido por el usuario y después muestre en
pantalla la suma de todos los enteros desde 1 hasta N. La suma de los N primeros enteros positivos
puede ser calculada de la siguiente forma:

"""
num_entero = int(input("Ingrese un numero entero positivo: "))
suma = num_entero * (num_entero + 1) // 2
print(f"La suma de {num_entero} es igual a {suma}")