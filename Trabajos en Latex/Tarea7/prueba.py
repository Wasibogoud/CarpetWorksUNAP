class NuevoLenguajeInterpreter:
    def __init__(self):
        self.variables = {}

    def asignar_variable(self, nombre, valor):
        self.variables[nombre] = valor

    def obtener_variable(self, nombre):
        if nombre in self.variables:
            return self.variables[nombre]
        else:
            raise ValueError(f"La variable '{nombre}' no está definida")

    def interpretar(self, codigo):
        tokens = codigo.split()
        i = 0
        while i < len(tokens):
            token = tokens[i]
            if token == "-":
                var1 = tokens[i-1]
                var2 = tokens[i+1]
                resultado = self.obtener_variable(var1) + self.obtener_variable(var2)
                self.asignar_variable(var1, resultado)
                del tokens[i:i+2]  # Eliminar el operador y la segunda variable
                i -= 1  # Retroceder el índice para compensar el cambio en la lista de tokens
            elif token == "=":
                self.asignar_variable(tokens[i-1], int(tokens[i+1]))
                del tokens[i-1:i+2]  # Eliminar la variable y el operador de asignación
                i -= 2  # Retroceder el índice
            i += 1

# Ejemplo de uso
interpreter = NuevoLenguajeInterpreter()
interpreter.interpretar("a = 5")
interpreter.interpretar("b = 3")
interpreter.interpretar("c = a - b")
print(interpreter.obtener_variable("c"))  # Imprime 8
