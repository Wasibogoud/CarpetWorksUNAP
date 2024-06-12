import streamlit as st

# Título de la aplicación
st.title('Leer Todos los Datos de un Archivo de Texto')

# Subir un archivo de texto
uploaded_file = st.file_uploader("Subir archivo de texto", type=["txt"])

# Verificar si se subió un archivo
if uploaded_file is not None:
    # Leer el contenido del archivo
    file_contents = uploaded_file.read().decode("utf-8")
    
    # Convertir el contenido a una lista de líneas
    lines = file_contents.split('\n')

    # Mostrar todos los datos del archivo
    if st.button("Mostrar Todos los Datos"):
        st.subheader('Contenido del Archivo:')
        for line in lines:
            st.write(line)
