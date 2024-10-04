import os
import re


def preprocesar_archivo(input_path: str, output_path: str):
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"El archivo {input_path} no existe.")

    with open(input_path, 'r') as infile:
        lines = infile.readlines()

    cleaned_code = []

    for line in lines:
        # Eliminar comentarios y espacios en blanco al final de la línea
        cleaned_line = line.split('#')[0].strip()

        # Solo añadir la línea si no está vacía
        if cleaned_line:
            # Insertar espacios alrededor de operadores y paréntesis
            cleaned_line = re.sub(r'(\S)([=+><():])(\S)', r'\1 \2 \3', cleaned_line)
            cleaned_line = re.sub(r'([=+><():])', r' \1 ', cleaned_line)
            cleaned_code.append(cleaned_line)

    # Unir todas las líneas en una sola, separadas por un espacio
    final_output = ' '.join(cleaned_code)

    # Escribir el resultado final en el archivo de salida
    with open(output_path, 'w') as outfile:
        outfile.write(final_output)

    print(f"Archivo procesado y guardado en {output_path}")

