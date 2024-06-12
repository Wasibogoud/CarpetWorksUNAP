import streamlit as st
import pandas as pd

# Definir una clase para el análisis
class DataHandler:
    def __init__(self, data): # Inicializar la clase con el DataFrame de pandas
        self.__data = data

    def load_data(self): # Cargar los datos del archivo CSV en un DataFrame de pandas.
        return pd.read_csv(self.__data)
    
    def preview(self): # Mostrar las primeras 10 filas del DataFrame.
        return self.__data.head(10)

    def describe_dataset(self):
        return self.__data.describe()

    
def main():
    st.title("Taller Practico - 1")
    
    # Subir archivo CSV
    archivo = st.file_uploader("Elija un archivo de texto con la matriz", type="csv")

    if archivo is not None:
        # Cargar el archivo CSV en un DataFrame
        df = pd.read_csv(archivo)

        # Instanciar el objeto DataHandler con el DataFrame cargado
        data_handler = DataHandler(df)

        # Mostrar las primeras 10 filas del DataFrame
        st.subheader("Vista Previa de los Datos (primeras 10 filas)")
        st.write(data_handler.preview())

        # Mostrar descripción del dataset
        st.subheader("Descripción del Dataset")
        st.write(data_handler.describe_dataset())

if __name__ == "__main__":
    main()
