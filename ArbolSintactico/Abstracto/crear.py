from ArbolSintactico.Abstracto import NodoNumero, NodoIdentificador, NodoOperador


def construir_ast(lista_tokens):
    pila = []
    nodo_actual = None
    for token in lista_tokens:
        if token.tipo == "Número Entero" or token.tipo == "Número Decimal":
            nodo_numero = NodoNumero(token.valor)
            pila.append(nodo_numero)
        elif token.tipo == "ID":
            nodo_identificador = NodoIdentificador(token.valor)
            pila.append(nodo_identificador)
        elif token.tipo == "Operador":
            nodo_operador = NodoOperador(token.valor)
            if len(pila) >= 2:
                derecho = pila.pop()
                izquierdo = pila.pop()
                nodo_operador.agregar_hijo(izquierdo)
                nodo_operador.agregar_hijo(derecho)
            pila.append(nodo_operador)
    if pila:
        nodo_actual = pila.pop()
    return nodo_actual