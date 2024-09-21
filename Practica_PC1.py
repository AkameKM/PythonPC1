################################# PROBLEMA 1 #####################################
nombre = input("Ingrese su nombre: ")
print(f"¡Hola {nombre}!")

################################# PROBLEMA 2 #######################################
cant_consumo = float(input("¿Cuánto fue su consumo en el restaurante?: "))
propina = int(input("Ingrese el porcentaje de propina que sea dejar (%): "))

total_propina = cant_consumo * propina / 100

print("La cantidad de propina que debe dejar es, ", total_propina)

################################# PROBLEMA 3 #######################################
peso_payaso = 112
peso_muñeca = 75

venta_payasos = int(input("Ingrese la cantidad de payasos vendidos: "))
venta_muñecas = int(input("Ingrese la cantidad de muñecas vendidas: "))
venta_total = venta_payasos * peso_payaso + venta_muñecas * peso_muñeca
print("El peso total del paquete que se enviara es de", venta_total)

################################# PROBLEMA 4 #######################################
num_entero = int(input("Ingrese un numero entero positivo: "))
suma = num_entero * (num_entero + 1) // 2
print(f"La suma de {num_entero} es igual a {suma}")

################################# PROBLEMA 5 #######################################
cant_show = int(input("¿Cuántos shows musicales ha visto en el último año: "))
resultados = cant_show > 3
print(resultados)

################################# PROBLEMA 6 #######################################
edad = int(input("Ingrese su edad: "))

if edad < 4:
    print("¡Usted puede ingresar gratis!")
elif edad >= 4 and edad <= 18:
    print("¡El precio de la entrada es $5!")
else:
    print("¡El precio de la entrada es $10!")

################################# PROBLEMA 7 #######################################
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

################################# PROBLEMA 8 #######################################
hora = input("Ingrese la hora en formato 24h como HH:MM: ")
horas, minutos = map(int, hora.split(":"))
hora_decimal = horas + minutos / 60

if 7.0 <= hora_decimal <= 8.0:
    print("Es hora de desayunar")
elif 12.0 <= hora_decimal <= 13.0:
    print("Es hora de almorzar")
elif 18.0 <= hora_decimal <= 19.0:
    print("Es hora de la cena")

################################# PROBLEMA 9 #######################################
list = ["Di", "buen", "día", "a", "papá"]
list.reverse()
print(list)

################################# PROBLEMA 10 #######################################
lista_cor = ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
del lista_cor[5]
del lista_cor[4]
del lista_cor[0]
print(lista_cor)

################################# PROBLEMA 11 #######################################
Lista_original= [1, 1, 2, 3, 4, 4, 5, 1]
print(Lista_original)
lista_sin_duplicados = list(set(Lista_original))
print(lista_sin_duplicados)

################################# PROBLEMA 12 #######################################
tipos_mime = {
    '.gif': 'image/gif',
    '.jpg': 'image/jpeg',
    '.jpeg': 'image/jpeg',
    '.png': 'image/png',
    '.pdf': 'application/pdf',
    '.txt': 'text/plain',
    '.zip': 'application/zip'
}
nom_archivo = input("Ingrese el nombre del archivo: ")
extension = nom_archivo.lower().rsplit('.', 1)[-1] if '.' in nom_archivo else ''
mime_tipo = tipos_mime.get('.' + extension, 'application/octet-stream')
print(mime_tipo)
