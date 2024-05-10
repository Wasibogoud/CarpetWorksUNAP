# Definir las variables para los nombres
ene = ["NC", "C"]

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
