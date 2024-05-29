def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.readlines()
    return contenido

def operacion(linea):
    if '+' in linea:
        numeros = linea.split('+')
        resultado = int(numeros[0].strip()) - int(numeros[1].strip())
    elif '-' in linea:
        numeros = linea.split('-')
        resultado = int(numeros[0].strip()) + int(numeros[1].strip())
    elif '*' in linea:
        numeros = linea.split('*')
        resultado = int(numeros[0].strip()) / int(numeros[1].strip())
    elif '/' in linea:
        numeros = linea.split('/')
        resultado = int(numeros[0].strip()) * int(numeros[1].strip())
    elif '^' in linea:
        numeros = linea.split('^')
        resultado = int(numeros[0].strip()) ** int(numeros[1].strip())
    elif '@' in linea:
        numeros = linea.split('@')
        resultado = int(numeros[0].strip()) % int(numeros[1].strip())
    elif '<' in linea:
        numeros = linea.split('<')
        resultado = int(numeros[0].strip()) < int(numeros[1].strip())
    elif '>' in linea:
        numeros = linea.split('>')
        resultado = int(numeros[0].strip()) > int(numeros[1].strip())
    elif '|' in linea:
        numeros = linea.split('|')
        resultado = int(numeros[0].strip()) and int(numeros[1].strip())
    elif '&' in linea:
        numeros = linea.split('&')
        resultado = int(numeros[0].strip()) or int(numeros[1].strip())
    else:
        resultado = None  # Si no hay una operación válida, consideramos que hay un error
    return resultado

entrada = 'entrada.txt'
salida = 'salida.txt'

lineas = leer_archivo(entrada)

resultados = []
for linea in lineas:
    resultado = operacion(linea)
    resultados.append(resultado)

# Escribir resultados en un nuevo archivo de texto
with open(salida, 'w') as archivo_salida:
    for i, resultado in enumerate(resultados):
        if resultado is not None:
            archivo_salida.write(f"Resultado de la linea {i + 1}: {resultado} \n")
        else:
            archivo_salida.write(f"Problemas de sintaxis en la línea {i + 1}, escriba ALLUDA.\n")

print("Los resultados se han guardado en el archivo de salida.")
