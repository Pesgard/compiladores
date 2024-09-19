from preprocesador.preprocesador import preprocesar_archivo
from preprocesador.recorrerArchivo import recorrer_archivo


def main():
    input_path = 'files/input.txt'
    output_path = 'files/output.txt'

    # Preprocesar el archivo
    preprocesar_archivo(input_path, output_path)

    # Recorrer el archivo preprocesado
    recorrer_archivo(output_path)

if __name__ == "__main__":
    main()
