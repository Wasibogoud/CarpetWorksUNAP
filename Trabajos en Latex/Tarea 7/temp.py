import numpy as np

# Función para obtener los coeficientes del polinomio
def obtener_coeficientes():
    n = int(input("Ingrese el grado del polinomio (n): "))
    coeficientes = []

    for i in range(n + 1):
        fraccion = input(f"Ingrese el coeficiente de x^{i} (formato a/b): ")
        numerador, denominador = map(int, fraccion.split('/'))
        coeficientes.append((numerador, denominador))

    return coeficientes

# Función para evaluar el polinomio en un punto dado x
def evaluar_polinomio(coeficientes, x):
    resultado = 0.0

    for i, (numerador, denominador) in enumerate(coeficientes):
        resultado += (numerador / denominador) * (x ** i)

    return resultado

# Función para encontrar intervalos alrededor de las raíces reales dentro de un epsilon dado
def encontrar_intervalos_raices(coeficientes, epsilon):
    intervalos = []

    # Iterar a través de un rango de valores para encontrar cambios de signo en el polinomio
    x = -1000.0
    while x <= 1000.0:
        fx = evaluar_polinomio(coeficientes, x)
        fx_next = evaluar_polinomio(coeficientes, x + epsilon)

        if fx * fx_next <= 0:  # Cambio de signo detectado, raíz potencial encontrada
            a = x
            b = x + epsilon

            # Refinar el intervalo utilizando el método de la bisección
            while abs(b - a) > epsilon:
                c = (a + b) / 2
                fc = evaluar_polinomio(coeficientes, c)

                if fx * fc < 0:
                    b = c
                else:
                    a = c

            intervalos.append((a, b))

        x += epsilon

    return intervalos

# Función para imprimir el polinomio
def imprimir_polinomio(coeficientes):
    terminos = []
    for i, (numerador, denominador) in enumerate(coeficientes):
        if numerador != 0:
            terminos.append(f"{numerador}/{denominador} * x^{i}")

    polinomio = " + ".join(terminos)
    print(f"Polinomio: P(x) = {polinomio}")

# Función para visualizar el polinomio evaluado en un rango dado de valores x
def visualizar_polinomio(coeficientes, rango_inicio, rango_fin, paso):
    print("Visualización del polinomio:")
    print(" x      |   P(x)")
    print("-----------------")

    x = rango_inicio
    while x <= rango_fin:
        fx = evaluar_polinomio(coeficientes, x)
        print(f"{x:7.2f} | {fx:7.2f}")
        x += paso

# Función para encontrar y ordenar las raíces reales
def encontrar_y_ordenar_raices(coeficientes, epsilon):
    raices = []

    # Encontrar las raíces dentro de cada intervalo
    intervalos = encontrar_intervalos_raices(coeficientes, epsilon)
    for a, b in intervalos:
        # Aplicar el método de la bisección para encontrar la raíz
        while abs(b - a) > epsilon:
            c = (a + b) / 2
            fc = evaluar_polinomio(coeficientes, c)

            if fc == 0.0:  # Raíz encontrada
                raices.append(c)
                break
            elif fc * evaluar_polinomio(coeficientes, a) < 0:
                b = c
            else:
                a = c

    # Ordenar las raíces de menor a mayor
    raices.sort()

    return raices

def main():
    coeficientes = obtener_coeficientes()

    # 2. Imprimir el polinomio
    imprimir_polinomio(coeficientes)

    # 3. Encontrar intervalos con un epsilon dado para cada raíz real
    epsilon = float(input("Ingrese el valor de epsilon para encontrar los intervalos de raices (E): "))

    intervalos = encontrar_intervalos_raices(coeficientes, epsilon)

    # Mostrar los intervalos de raíces encontrados
    print("\nIntervalos alrededor de las raices reales:")
    for a, b in intervalos:
        print(f"[{a}, {b}]")

    # 4. Visualizar el polinomio
    rango_inicio, rango_fin, paso = map(float, input("\nIngrese el rango de valores x para visualizar el polinomio (inicio fin paso): ").split())

    visualizar_polinomio(coeficientes, rango_inicio, rango_fin, paso)

    # 5. Encontrar y ordenar las raíces reales
    raices = encontrar_y_ordenar_raices(coeficientes, epsilon)

    # 6. Imprimir las raíces de menor a mayor
    print("\nRaices reales encontradas (ordenadas de menor a mayor):")
    for raiz in raices:
        print(raiz)

if __name__ == "__main__":
    main()
