class ValidadorSintactico:
    """Clase para realizar validaciones sintácticas según la gramática del lenguaje."""

    @staticmethod
    def buscar_cierre_parentesis(nodo_inicial):
        """
        Busca el paréntesis de cierre ')' correspondiente a partir de un nodo inicial.
        Devuelve:
        - True si se encuentra el cierre.
        - Nodo donde se encuentra el cierre.
        - Posición del nodo desde el nodo inicial.
        """
        nodo_actual = nodo_inicial
        balance = 0

        while nodo_actual:
            token_actual = nodo_actual.token
            if token_actual.lexema == "(":
                balance += 1
            elif token_actual.lexema == ")":
                balance -= 1
                if balance == 0:
                    return True, nodo_actual

            nodo_actual = nodo_actual.siguiente

        return False, None

    @staticmethod
    def verificar_errores(lista_tokens):
        """Valida errores sintácticos."""
        errores = []
        nodo_actual = lista_tokens.primero

        while nodo_actual:
            token_actual = nodo_actual.token

            # Validación de palabras reservadas que requieren paréntesis y ':'
            if token_actual.tipo == "Palabra Reservada" and token_actual.lexema in ["si", "mientras", "sino"]:
                siguiente = nodo_actual.siguiente
                if token_actual.lexema in ["si", "mientras"] and (not siguiente or siguiente.token.lexema != "("):
                    errores.append(
                        f"Error sintáctico en línea {token_actual.renglon}, columna {token_actual.columna}: "
                        f"Se esperaba '(' después de '{token_actual.lexema}'."
                    )
                else:
                    # Buscar cierre de paréntesis
                    cierre_encontrado, nodo_cierre = ValidadorSintactico.buscar_cierre_parentesis(siguiente)
                    if not cierre_encontrado:
                        errores.append(
                            f"Error sintáctico en línea {siguiente.token.renglon}, columna {siguiente.token.columna}: "
                            f"No se encontró el cierre de paréntesis ')' correspondiente para '{token_actual.lexema}'."
                        )
                    else:
                        # Validar que después del cierre de paréntesis haya un ':'
                        siguiente_despues_cierre = nodo_cierre.siguiente
                        if not siguiente_despues_cierre or siguiente_despues_cierre.token.lexema != ":":
                            errores.append(
                                f"Error sintáctico en línea {nodo_cierre.token.renglon}, columna {nodo_cierre.token.columna + 1}: "
                                f"Se esperaba ':' después del paréntesis de cierre ')'."
                            )
            # Validación de asignaciones
            if token_actual.tipo == "ID":  # Identificador encontrado
                siguiente = nodo_actual.siguiente  # Nodo siguiente
                if siguiente:
                    siguiente_token = siguiente.token
                    # Caso 1: Identificador seguido directamente por un valor (falta `=`)
                    if siguiente_token.tipo in ["Número Entero", "Número Decimal", "Cadena"]:
                        errores.append(
                            f"Error sintáctico en línea {token_actual.renglon}, columna {token_actual.columna + len(token_actual.lexema)}: "
                            f"Falta el operador '=' entre el identificador '{token_actual.lexema}' y el valor '{siguiente_token.lexema}'."
                        )
                    # Caso 2: Identificador seguido por `=` pero sin un valor después
                    elif siguiente_token.lexema == "=":
                        valor = siguiente.siguiente if siguiente.siguiente else None
                        if not valor or valor.token.tipo not in ["ID", "Número Entero", "Número Decimal", "Cadena"]:
                            errores.append(
                                f"Error sintáctico en línea {siguiente_token.renglon}, columna {siguiente_token.columna}: "
                                f"Se esperaba un valor después del '=' en la asignación."
                            )
            nodo_actual = nodo_actual.siguiente

        return errores
