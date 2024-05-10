# Definir las variables para los nombres
ene = ["NC", "C"]
ce = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# Crear el diccionario con las variables asignadas a las claves correspondientes
reglas = {'N': ene, 'C': ce}

# Solicitar al usuario que ingrese un número y convertirlo en una cadena
X = str(input("Inserte un numero: "))

# Obtener la longitud de la cadena X
n = len(X)

# Inicializar la cadena con "NC"
cadena = ene[0]

# Imprimir el paso inicial
print("1.", cadena)

# Inicializar el índice del bucle
i = 2

# Mientras el índice sea menor o igual que la longitud del número
while i < n:
    # Si la letra actual es una "N", reemplazarla por "NC"
    if cadena[-1] == "N":
        cadena += ene[0]
    else:
        cadena += ene[1]
    # Imprimir el paso actual del procedimiento
    print(i, ".", cadena)
    # Incrementar el índice
    i += 1

# Imprimir la cadena generada
print("Cadena generada:", cadena)

# Reemplazar la primera "N" por "C" en la cadena generada
cadena = cadena.replace("N", "C", 1)

print("Resultado intermedio:", cadena)

# Recorrer la cadena y reemplazar cada "C" por el valor ingresado por el usuario
for index, char in enumerate(X):
    if cadena[index] == "C":
        cadena = cadena[:index] + char + cadena[index + 1:]
        print(i, ".", cadena)
        i += 1

print("Resultado final:", cadena)
