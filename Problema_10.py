"""
Escriba un programa para imprimir una lista específica después de eliminar los elementos que se
encuentran en la posición 0, 4 y 5.
lista de muestra: ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
Resultado esperado: ['Verde', 'Blanco', 'Negro']

"""

lista_cor = ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
del lista_cor[5]
del lista_cor[4]
del lista_cor[0]
print(lista_cor)