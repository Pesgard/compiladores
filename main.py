from preprocesador.preprocesador import preprocesar_archivo
from AnalizadorLexico.AnalizadorLexico import ListaEnlazada
from Automatas.automataEnteros import AutomataEnteros
from Automatas.automataDecimales import AutomataDecimales
from Automatas.palabrasReservadas import AutomataPalabrasReservadas
from Automatas.identificadores import AutomataIdentificadores
from Automatas.OperadoresLogicos import AutomataOperadoresLogicos, AutomataOperadoresAritmeticos

def clasificar_palabra(palabra):
    automata_enteros = AutomataEnteros()
    automata_decimales = AutomataDecimales()
    automata_palabras_reservadas = AutomataPalabrasReservadas()
    automata_identificadores = AutomataIdentificadores()
    automata_operadores_logicos = AutomataOperadoresLogicos()
    automata_operadores_aritmeticos = AutomataOperadoresAritmeticos()

    if automata_enteros.procesar_cadena(palabra):
        return "Número Entero"
    elif automata_decimales.procesar_cadena(palabra):
        return "Número Decimal"
    elif automata_palabras_reservadas.procesar_cadena(palabra):
        return "Palabra Reservada"
    elif automata_identificadores.procesar_cadena(palabra):
        return "ID"
    elif automata_operadores_logicos.procesar_cadena(palabra):
        return "Operador Lógico"
    elif automata_operadores_aritmeticos.procesar_cadena(palabra):
        return "Operador Aritmético"
    else:
        return "Desconocido"

def analizar_archivo(archivo):
    lista_tokens = ListaEnlazada()
    with open(archivo, 'r') as file:
        palabras = file.read().split()

    for palabra in palabras:
        tipo = clasificar_palabra(palabra)
        lista_tokens.agregar_token(palabra, tipo)

    return lista_tokens

if __name__ == "__main__":
    # input_path = 'files/input.txt'
    output_path = 'files/output.txt'
    #
    # # Preprocesa el archivo de entrada y guarda el resultado en el archivo de salida
    # preprocesar_archivo(input_path, output_path)

    # Analiza el archivo preprocesado y genera los tokens
    lista_tokens = analizar_archivo(output_path)
    lista_tokens.imprimir_lista()