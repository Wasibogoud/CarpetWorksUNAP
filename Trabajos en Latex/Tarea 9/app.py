import streamlit as st
import matplotlib.pyplot as plt
import random

# Función para simular el paso del tiempo
def simular_paso_tiempo(n_ovejas, n_zorros, n_anios, seed=None):
    if seed is not None:
        random.seed(seed)  # Establecer la semilla aleatoria

    ovejas = [n_ovejas]  # Inicializamos la lista de ovejas con la población inicial
    zorros = [n_zorros]  # Inicializamos la lista de zorros con la población inicial
    meses_por_anio = 12

    for anio in range(1, n_anios + 1):
        for mes in range(1, meses_por_anio + 1):
            # Calcular el número de ovejas y zorros que mueren este mes
            n_muertes_ovejas = 0
            for i, edad in enumerate(edades_ovejas):
                if edad and 6 <= edad <= 8:
                    n_muertes_ovejas += 1
                    edades_ovejas[i] = None  # Marcar la oveja como muerta
            ovejas[-1] -= n_muertes_ovejas

            n_muertes_zorros = 0
            for i, edad in enumerate(edades_zorros):
                if edad and 3 <= edad <= 4:
                    n_muertes_zorros += 1
                    edades_zorros[i] = None  # Marcar el zorro como muerto
            zorros[-1] -= n_muertes_zorros

            # Procreación de ovejas (cada 365 días)
            if mes % 12 == 0:
                n_nuevas_ovejas = sum(1 for edad in edades_ovejas if edad and edad >= 1)
                ovejas.append(ovejas[-1] + n_nuevas_ovejas)
                edades_ovejas.extend([0] * n_nuevas_ovejas)

            # Procreación de zorros (cada 120 días)
            if mes % 4 == 0:
                n_nuevos_zorros = sum(1 for edad in edades_zorros if edad and edad >= 1)
                zorros[-1] += n_nuevos_zorros
                edades_zorros.extend([0] * n_nuevos_zorros)

            # Envejecer ovejas y zorros
            for i, edad in enumerate(edades_ovejas):
                if edad:
                    edades_ovejas[i] += 1

            for i, edad in enumerate(edades_zorros):
                if edad:
                    edades_zorros[i] += 1

            # Predación de zorros (cada 120 días)
            if mes % 4 == 0:
                n_zorros = min(ovejas[-1] // 2, zorros[-1])  # Los zorros comen ovejas jóvenes
                ovejas[-1] -= n_zorros
                zorros[-1] -= n_zorros

    return ovejas, zorros

# Función para graficar la evolución de la población
def graficar_poblacion(ovejas, zorros):
    plt.figure(figsize=(10, 6))
    plt.plot(range(len(ovejas)), ovejas, label='Ovejas', color='blue')
    plt.plot(range(len(zorros)), zorros, label='Zorros', color='red')
    plt.xlabel('Mes')
    plt.ylabel('Población')
    plt.title('Evolución de la población de ovejas y zorros')
    plt.legend()
    st.pyplot()

# Interfaz de usuario con Streamlit
st.title('Simulación de población de ovejas y zorros')

n_ovejas = st.number_input('Ingrese el número inicial de ovejas:', min_value=0, step=1, value=50)
n_zorros = st.number_input('Ingrese el número inicial de zorros:', min_value=0, step=1, value=10)
n_anios = st.number_input('Ingrese la duración de la simulación en años:', min_value=1, step=1, value=5)
semilla = st.number_input('Ingrese una semilla aleatoria (opcional):', min_value=0, step=1)

if st.button('Simular'):
    # Inicializar edades de ovejas y zorros
    edades_ovejas = [random.randint(1, 8) for _ in range(n_ovejas)]
    edades_zorros = []

    ovejas, zorros = simular_paso_tiempo(n_ovejas, n_zorros, n_anios, seed=semilla)
    graficar_poblacion(ovejas, zorros)