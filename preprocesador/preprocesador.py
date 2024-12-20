import os
import re


def preprocesar_archivo(input_path: str, output_path: str):
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"El archivo {input_path} no existe.")

    with open(input_path, 'r') as infile:
        lines = infile.readlines()

    cleaned_code = []

    for line in lines:
        # Eliminar comentarios
        cleaned_line = line.split('#')[0].strip()

        # Solo procesar líneas no vacías
        if cleaned_line:
            # Insertar espacios alrededor de operadores y paréntesis, excepto en "sino:"
            if not cleaned_line.startswith("sino:"):
                cleaned_line = re.sub(r'([=+><():])', r' \1 ', cleaned_line)
            # Reducir múltiples espacios consecutivos a uno
            cleaned_line = re.sub(r'\s+', ' ', cleaned_line).strip()
            cleaned_code.append(cleaned_line)

    # Mantener la estructura en líneas separadas
    formatted_code = []
    for line in cleaned_code:
        # Añadir línea vacía antes de estructuras clave para mejor legibilidad
        if re.match(r'\b(si|sino|mientras|escribir)\b', line):
            if formatted_code and formatted_code[-1] != "":  # Evitar líneas en blanco duplicadas
                formatted_code.append("")
        formatted_code.append(line)

    # Escribir el resultado al archivo de salida
    with open(output_path, 'w') as outfile:
        outfile.write('\n'.join(formatted_code) + '\n')  # Asegurar salto de línea al final

    print(f"Archivo procesado y guardado en {output_path}")
