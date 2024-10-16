class AutomataEnteros:
    def __init__(self):
        # Estado inicial del autómata
        self.estado_inicial = 0
        # Conjunto de estados de aceptación
        self.estados_aceptacion = {1}
        # Diccionario de transiciones: del estado 0 a 1 para el primer dígito, y de 1 a 1 para los siguientes dígitos
        self.transiciones = {
            0: {str(i): 1 for i in range(10)},
            1: {str(i): 1 for i in range(10)}
        }
        # Estado actual del autómata
        self.estado_actual = self.estado_inicial

    def reiniciar(self):
        # Reinicia el estado actual al estado inicial
        self.estado_actual = self.estado_inicial

    def procesar_caracter(self, caracter):
        # Procesa un carácter y actualiza el estado actual
        if caracter in self.transiciones[self.estado_actual]:
            self.estado_actual = self.transiciones[self.estado_actual][caracter]
        else:
            # Si el carácter no es válido, el estado actual se vuelve None
            self.estado_actual = None

    def es_aceptado(self):
        # Verifica si el estado actual es un estado de aceptación
        return self.estado_actual in self.estados_aceptacion

    def procesar_cadena(self, cadena):
        # Reinicia el autómata antes de procesar la cadena
        self.reiniciar()
        # Procesa cada carácter de la cadena
        for caracter in cadena:
            self.procesar_caracter(caracter)
            # Si el estado actual es None, la cadena no es aceptada
            if self.estado_actual is None:
                return False
        # Retorna True si la cadena es aceptada, False en caso contrario
        return self.es_aceptado()


# # Ejemplo de uso
# automata = AutomataEnteros()
# cadena = "12a"  # Cadena a ser procesada
# if automata.procesar_cadena(cadena):
#     print(f"La cadena '{cadena}' es un número entero válido.")
# else:
#     print(f"La cadena '{cadena}' no es un número entero válido.")