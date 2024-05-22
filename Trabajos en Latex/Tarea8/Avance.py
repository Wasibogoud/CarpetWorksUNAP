import os

# Cambia al directorio donde se encuentra el archivo
os.chdir('E:/UNAP/UNAP-IV/LENGUAJES DE PROGRAMACION II/Trabajos en Latex/Tarea8/')

# Abre el archivo
with open('a.txt', 'r') as archivo:
    contenido = archivo.read()

print(contenido)