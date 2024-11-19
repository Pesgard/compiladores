from ArbolSintactico.Abstracto import NodoNumero, NodoIdentificador, NodoOperador


def construir_ast(lista_tokens):
    pila = []
    nodo_actual = None
    for token in lista_tokens:
        print(f"Procesando token: {token.valor} ({token.tipo})")
        if token.tipo == "Número Entero" or token.tipo == "Número Decimal":
            nodo_numero = NodoNumero(token.valor)
            pila.append(nodo_numero)
            print(f"  Nodo número agregado a la pila: {nodo_numero.valor}")
        elif token.tipo == "ID":
            nodo_identificador = NodoIdentificador(token.valor)
            pila.append(nodo_identificador)
            print(f"  Nodo identificador agregado a la pila: {nodo_identificador.nombre}")
        elif token.tipo == "Operador":
            nodo_operador = NodoOperador(token.valor)
            if len(pila) >= 2:
                derecho = pila.pop()
                izquierdo = pila.pop()
                nodo_operador.agregar_hijo(izquierdo)
                nodo_operador.agregar_hijo(derecho)
                print(f"  Nodo operador creado: {nodo_operador.operador}")
                print(f"    Hijo izquierdo: {izquierdo}")
                print(f"    Hijo derecho: {derecho}")
            pila.append(nodo_operador)
            print(f"  Nodo operador agregado a la pila: {nodo_operador.operador}")
        elif token.tipo == "Palabra Reservada" and token.valor in ["if", "else"]:
            nodo_reservada = NodoOperador(token.valor)
            pila.append(nodo_reservada)
            print(f"  Nodo palabra reservada agregado a la pila: {nodo_reservada.operador}")
        print(f"  Estado de la pila: {[nodo.tipo for nodo in pila]}")
    if pila:
        nodo_actual = pila.pop()
    return nodo_actual
