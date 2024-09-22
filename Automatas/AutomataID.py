class AutomataDigitos:
    def __init__(self):
        # El autómata empieza en un estado "inicial"
        self.estado = 'inicial'

    def procesar(self, cadena):
        # Recorrer cada carácter en la cadena
        for caracter in cadena:
            # Estado inicial, sólo acepta dígitos
            if self.estado == 'inicial':
                if caracter.isdigit():  # Si es un dígito, cambiar al estado "digito"
                    self.estado = 'digito'
                else:
                    self.estado = 'error'  # Si no es un dígito, cambiar al estado "error"
                    break
            # Estado "digito", sigue aceptando solo dígitos
            elif self.estado == 'digito':
                if not caracter.isdigit():  # Si encontramos un carácter que no es un dígito, error
                    self.estado = 'error'
                    break

        # Si el autómata termina en estado "digito", la cadena es válida
        if self.estado == 'digito':
            return True
        else:
            return False

# Uso del autómata
automata = AutomataDigitos()
cadena = input("Introduce una cadena de dígitos: ")

# Procesamos la cadena
if automata.procesar(cadena):
    print("La cadena contiene solo dígitos.")
else:
    print("La cadena contiene caracteres no válidos.")

