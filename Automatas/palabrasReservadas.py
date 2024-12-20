class AutomataPalabrasReservadas:
    def __init__(self):
        self.estado_inicial = 0
        self.estados_aceptacion = {1}
        self.estado_actual = self.estado_inicial
        self.transiciones = {
            0: {},  # Este estado se llenará con transiciones al inicializar.
        }
        self.palabras_reservadas = {
            "si", "sino", "mientras", "inicio", "fin", "UAS", "SURSUMVERSUS",
            "var", "const", "decimal", "entero", "cadena", "booleano", "escribir", "leer"
        }
        self.inicializar_transiciones()

    def inicializar_transiciones(self):
        for palabra in self.palabras_reservadas:
            estado = self.estado_inicial
            for caracter in palabra:
                if estado not in self.transiciones:
                    self.transiciones[estado] = {}
                if caracter not in self.transiciones[estado]:
                    nuevo_estado = len(self.transiciones)
                    self.transiciones[estado][caracter] = nuevo_estado
                estado = self.transiciones[estado][caracter]
            # Marcar el último estado como de aceptación
            if estado not in self.transiciones:
                self.transiciones[estado] = {}
            self.transiciones[estado]['aceptacion'] = True

    def reiniciar(self):
        self.estado_actual = self.estado_inicial

    def procesar_cadena(self, cadena):
        self.reiniciar()
        for caracter in cadena:
            if self.estado_actual not in self.transiciones or caracter not in self.transiciones[self.estado_actual]:
                self.estado_actual = None
                break
            self.estado_actual = self.transiciones[self.estado_actual][caracter]
        return self.es_aceptado()

    def es_aceptado(self):
        return self.estado_actual is not None and 'aceptacion' in self.transiciones[self.estado_actual]
