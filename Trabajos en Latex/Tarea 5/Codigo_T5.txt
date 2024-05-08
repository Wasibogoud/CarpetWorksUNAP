import random

cerradas = ["4", "6", "8", "9", "0", "q", "o", "p", "a", "d", "g", "b"]

def generar_combinaciones(valores, p, combinacion_actual=""):
    if p == 0:
        print(combinacion_actual)
        return
    for valor in valores:
        generar_combinaciones(valores, p - 1, combinacion_actual + valor)

n = int(input("Ingrese tamaño: "))

if n <= 0 or n > len(cerradas):
    print("Por favor, ingrese un número positivo mayor que cero y menor o igual que", len(cerradas))
else:
    valores_seleccionados = random.sample(cerradas, n)
    print("Valores seleccionados:", valores_seleccionados)

    p_max = int(input("Ingrese la longitud máxima de las combinaciones: "))
    if p_max <= 0:
        print("Por favor, ingrese un número positivo mayor que cero para la longitud de las combinaciones.")
    else:
        print("Combinaciones:")
        for p in range(1, p_max + 1):
            print("Combinaciones de longitud", p)
            generar_combinaciones(valores_seleccionados, p)
            print()  # Agrega una línea en blanco después de cada conjunto de combinaciones
