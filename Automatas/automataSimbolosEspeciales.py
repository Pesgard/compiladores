# Autómata para símbolos especiales
class AutomataSimbolosEspeciales:
    def __init__(self):
        self.simbolos_especiales = {'(', ')', '{', '}', '[', ']', ',', '"', ':',}

    def procesar_cadena(self, cadena):
        return cadena in self.simbolos_especiales
