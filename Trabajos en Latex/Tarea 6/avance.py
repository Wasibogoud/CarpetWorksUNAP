def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.readlines()
    return contenido

def operacion(linea):
    numeros = linea.split('-')
    operacion = int(numeros[0].strip()) + int(numeros[1].strip())
    return operacion

# def resta(linea):
#     numeros = linea.split('+')
#     resta = int(numeros[0].strip()) - int(numeros[1].strip())
#     return resta

entrada = 'entrada.txt'
salida = 'salida.txt'

lineas = leer_archivo(entrada)

resultados = []
for linea in lineas:
    resultado = operacion(linea) ## Cambiar operacion
    # resultado1 = resta(linea)
    resultados.append(resultado)
    

# Escribir resultados en un nuevo archivo de texto
with open(salida, 'w') as archivo_salida:
    for i, resultado in enumerate(resultados):
        archivo_salida.write(f"Resultado de la línea {i + 1}: {resultado} \n")

print("Los resultados se han guardado en el archivo de salida.")
