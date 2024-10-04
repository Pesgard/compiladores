# Clase para representar un token
class Token:
    def __init__(self, id, lexema, tipo):
        self.id = id
        self.lexema = lexema
        self.tipo = tipo

# Clase para representar un nodo de la lista enlazada
class Nodo:
    def __init__(self, token):
        self.token = token
        self.anterior = None
        self.siguiente = None

# Clase para manejar la lista enlazada de tokens
class ListaEnlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.id_actual = 0

    def agregar_token(self, lexema, tipo):
        nuevo_token = Token(self.id_actual, lexema, tipo)
        nuevo_nodo = Nodo(nuevo_token)
        if self.primero is None:
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.ultimo
            self.ultimo.siguiente = nuevo_nodo
            self.ultimo = nuevo_nodo
        self.id_actual += 1

    def imprimir_lista(self):
        nodo_actual = self.primero
        while nodo_actual is not None:
            token = nodo_actual.token
            print(f"ID: {token.id}, Lexema: {token.lexema}, Tipo: {token.tipo}")
            nodo_actual = nodo_actual.siguiente