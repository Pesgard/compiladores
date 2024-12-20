class ValidadorSintactico:
    """Clase para realizar validaciones sintácticas según la gramática del lenguaje."""

    @staticmethod
    def verificar_errores(lista_tokens):
        """ Verifica errores sintácticos según la gramática del lenguaje. """
        errores = []
        nodo_actual = lista_tokens.primero  # Comenzar desde el primer nodo

        # Validación de inicio del programa
        if not nodo_actual or nodo_actual.token.tipo != "Palabra Reservada" or nodo_actual.token.lexema != "UAS":
            errores.append("Error sintáctico: El programa debe comenzar con 'UAS'.")
        else:
            nodo_actual = nodo_actual.siguiente  # Avanzar al siguiente nodo si ya validamos el inicio

        # Recorrer los tokens y validar errores
        while nodo_actual:
            token_actual = nodo_actual.token  # Obtener el token del nodo actual

            # Validación de ciclos
            if token_actual.tipo == "Palabra Reservada" and token_actual.lexema in ["mientras", "para"]:
                siguiente = nodo_actual.siguiente.token if nodo_actual.siguiente else None
                if not siguiente or siguiente.lexema != "(":
                    errores.append(
                        f"Error sintáctico en línea {token_actual.renglon}, columna {token_actual.columna}: "
                        f"Se esperaba '(' después de '{token_actual.lexema}'."
                    )
                else:
                    # Validar cierre de paréntesis
                    cierre_encontrado, _, _ = ValidadorSintactico.buscar_cierre_parentesis(nodo_actual.siguiente)
                    if not cierre_encontrado:
                        errores.append(
                            f"Error sintáctico en línea {token_actual.renglon}, columna {token_actual.columna}: "
                            f"No se encontró el cierre de paréntesis ')' correspondiente después de '{token_actual.lexema}'."
                        )

            # Validación de "si" y "sino"
            if token_actual.tipo == "Palabra Reservada" and token_actual.lexema == "si":
                siguiente = nodo_actual.siguiente.token if nodo_actual.siguiente else None
                if not siguiente or siguiente.lexema != "(":
                    errores.append(
                        f"Error sintáctico en línea {token_actual.renglon}, columna {token_actual.columna}: "
                        f"Se esperaba '(' después de 'si'."
                    )
                else:
                    cierre_encontrado, _, _ = ValidadorSintactico.buscar_cierre_parentesis(nodo_actual.siguiente)
                    if not cierre_encontrado:
                        errores.append(
                            f"Error sintáctico en línea {token_actual.renglon}, columna {token_actual.columna}: "
                            f"No se encontró el cierre de paréntesis ')' correspondiente después de 'si'."
                        )
            elif token_actual.tipo == "Palabra Reservada" and token_actual.lexema == "sino":
                anterior = nodo_actual.anterior.token if nodo_actual.anterior else None
                if not anterior or anterior.lexema != ":":
                    errores.append(
                        f"Error sintáctico en línea {token_actual.renglon}, columna {token_actual.columna}: "
                        f"'sino' debe seguir a un bloque 'si' terminado con ':'."
                    )

            # Validación de "escribir"
            if token_actual.tipo == "Palabra Reservada" and token_actual.lexema == "escribir":
                siguiente = nodo_actual.siguiente.token if nodo_actual.siguiente else None
                if not siguiente or siguiente.lexema != "(":
                    errores.append(
                        f"Error sintáctico en línea {token_actual.renglon}, columna {token_actual.columna}: "
                        f"Se esperaba '(' después de 'escribir'."
                    )
                else:
                    cierre_encontrado, _, _ = ValidadorSintactico.buscar_cierre_parentesis(nodo_actual.siguiente)
                    if not cierre_encontrado:
                        errores.append(
                            f"Error sintáctico en línea {token_actual.renglon}, columna {token_actual.columna}: "
                            f"No se encontró el cierre de paréntesis ')' correspondiente después de 'escribir'."
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

            nodo_actual = nodo_actual.siguiente  # Mover al siguiente nodo

        # Salida de errores
        return errores
