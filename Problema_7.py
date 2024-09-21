"""
Realiza un programa que lea dos números por teclado y permite elegir entre 3 opciones en un menú:
- Mostrar una suma de los dos números
- Mostrar una resta de los dos números (el primero menos el segundo)
- Mostrar una multiplicación de los dos números
- En caso de introducir una opción inválida, el programa informará de que no es correcta.

"""
num_1 = int(input("Ingrese primer numero: "))
num_2 = int(input("Ingrese segundo numero: "))

print("----- Elija una opción -----")
print("1.Mostrar una suma de los dos números")
print("2.Mostrar una resta de los dos números")
print("3.Mostrar una multiplicación de los dos números")

opcion_1 =  num_1 +  num_2
opcion_2 =  num_1 -  num_2
opcion_3 =  num_1 *  num_2

opcion = int(input("Ingrese la opción que desea: "))

if opcion == 1:
    print("El resultado de la suma es, ", opcion_1)
elif opcion == 2:
    print("El resultado de la resta es, ", opcion_2)
elif opcion == 3:
    print("El resultado de la multiplicación es, ", opcion_3)
else:
    print("Opción no válida. ¡Elegir entre 3 opciones del menú!")