from preprocesador.preprocesador import preprocesar_archivo
from preprocesador.recorrerArchivo import recorrer_archivo
from Automatas.automataEnteros import AutomataEnteros
from Automatas.automataDecimales import AutomataDecimales
from Automatas.palabrasReservadas import AutomataPalabrasReservadas
from Automatas.identificadores import AutomataIdentificadores


# Función para clasificar una palabra utilizando los autómatas definidos
def clasificar_palabra(palabra):
    automata_enteros = AutomataEnteros()
    automata_decimales = AutomataDecimales()
    automata_palabras_reservadas = AutomataPalabrasReservadas()
    automata_identificadores = AutomataIdentificadores()

    # Verifica si la palabra es un número entero
    if automata_enteros.procesar_cadena(palabra):
        return "Número Entero"
    # Verifica si la palabra es un número decimal
    elif automata_decimales.procesar_cadena(palabra):
        return "Número Decimal"
    # Verifica si la palabra es una palabra reservada
    elif automata_palabras_reservadas.procesar_cadena(palabra):
        return "Palabra Reservada"
    # Verifica si la palabra es un identificador
    elif automata_identificadores.procesar_cadena(palabra):
        return "Identificador"
    # Si no coincide con ninguna categoría, se clasifica como desconocido
    else:
        return "Desconocido"


# Función para clasificar todas las palabras en un archivo
def clasificar_archivo(archivo):
    # Abre el archivo y lee todas las palabras
    with open(archivo, 'r') as file:
        palabras = file.read().split()

    # Clasifica cada palabra utilizando la función clasificar_palabra
    clasificaciones = {palabra: clasificar_palabra(palabra) for palabra in palabras}

    # Imprime la clasificación de cada palabra
    for palabra, clasificacion in clasificaciones.items():
        print(f"{palabra}: {clasificacion}")


# Función principal del programa
def main():
    input_path = 'files/input.txt'
    output_path = 'files/output.txt'

    # Preprocesa el archivo de entrada y guarda el resultado en el archivo de salida
    preprocesar_archivo(input_path, output_path)

    # Recorre el archivo preprocesado y clasifica las palabras
    recorrer_archivo(output_path)


# Punto de entrada del programa
if __name__ == "__main__":
    # Llama a la función principal
    # main()
    # Clasifica las palabras en el archivo 'output.txt'
    clasificar_archivo('files/output.txt')
