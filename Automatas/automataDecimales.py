class AutomataDecimales:
    def __init__(self):
        # Estado inicial del autómata
        self.estado_inicial = 0
        # Conjunto de estados de aceptación
        self.estados_aceptacion = {2}
        # Diccionario de transiciones
        self.transiciones = {
            0: {str(i): 1 for i in range(10)},  # Del estado 0 a 1 para el primer dígito
            1: {str(i): 1 for i in range(10)}  # Del estado 1 a 1 para los siguientes dígitos
        }
        # Añadir transición del estado 1 al estado 2 con el punto
        self.transiciones[1]['.'] = 2
        # Añadir transiciones del estado 2 al estado 2 para los dígitos después del punto
        self.transiciones[2] = {str(i): 2 for i in range(10)}
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

