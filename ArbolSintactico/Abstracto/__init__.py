# Clase base para los nodos del AST
class NodoAST:
    def __init__(self, tipo):
        self.tipo = tipo
        self.hijos = []

    def agregar_hijo(self, nodo):
        self.hijos.append(nodo)

    def recorrer_inorden(self):
        resultado = []
        if len(self.hijos) == 2:
            resultado.extend(self.hijos[0].recorrer_inorden())
        resultado.append(self)
        if len(self.hijos) == 2:
            resultado.extend(self.hijos[1].recorrer_inorden())
        return resultado

# Clase para nodos de operadores
class NodoOperador(NodoAST):
    def __init__(self, operador):
        super().__init__("Operador")
        self.operador = operador

# Clase para nodos de números
class NodoNumero(NodoAST):
    def __init__(self, valor):
        super().__init__("Número")
        self.valor = valor

# Clase para nodos de identificadores
class NodoIdentificador(NodoAST):
    def __init__(self, nombre):
        super().__init__("Identificador")
        self.nombre = nombre