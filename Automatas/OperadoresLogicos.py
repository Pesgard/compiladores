# Autómata para operadores lógicos
class AutomataOperadoresLogicos:
    def __init__(self):
        self.operadores_logicos = {"&&", "||", "!"}

    def procesar_cadena(self, cadena):
        return cadena in self.operadores_logicos

# Autómata para operadores aritméticos
class AutomataOperadoresAritmeticos:
    def __init__(self):
        self.operadores_aritmeticos = {"+", "-", "*", "/", "%"}

    def procesar_cadena(self, cadena):
        return cadena in self.operadores_aritmeticos