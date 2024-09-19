class AutomataPalabrasReservadas:
    def __init__(self):
        # Estado inicial del autómata
        self.estado_inicial = 0
        # Conjunto de estados de aceptación
        self.estados_aceptacion = {1}
        # Lista de palabras reservadas
        self.palabras_reservadas = {
            "si", "sino", "mientras", "inicio", "fin", "UAS", "SURSUMVERSUS",
            "var", "const", "decimal", "entero", "cadena", "booleano", "escribir", "leer"
        }
        # Estado actual del autómata
        self.estado_actual = self.estado_inicial

    def reiniciar(self):
        # Reinicia el estado actual al estado inicial
        self.estado_actual = self.estado_inicial

    def procesar_cadena(self, cadena):
        # Reinicia el autómata antes de procesar la cadena
        self.reiniciar()
        # Verifica si la cadena es una palabra reservada
        if cadena in self.palabras_reservadas:
            self.estado_actual = 1
        else:
            self.estado_actual = None
        # Retorna True si la cadena es aceptada, False en caso contrario
        return self.es_aceptado()

    def es_aceptado(self):
        # Verifica si el estado actual es un estado de aceptación
        return self.estado_actual in self.estados_aceptacion


# Ejemplo de uso
automata = AutomataPalabrasReservadas()
cadena = "SURSUMVERSUS"  # Cadena a ser procesada
if automata.procesar_cadena(cadena):
    print(f"La cadena '{cadena}' es una palabra reservada válida.")
else:
    print(f"La cadena '{cadena}' no es una palabra reservada válida.")