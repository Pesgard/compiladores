import os


def preprocesar_archivo(input_path: str, output_path: str):
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"El archivo {input_path} no existe.")

    with open(input_path, 'r') as infile:
        lines = infile.readlines()

    cleaned_lines = []
    for line in lines:
        # Eliminar comentarios, espacios en blanco, líneas vacías y tabuladores
        cleaned_line = line.split('#')[0].strip()  # Eliminar comentarios y espacios en blanco
        if cleaned_line:  # Si la línea no está vacía después de limpiar
            cleaned_lines.append(cleaned_line.replace('\t', ''))  # Eliminar tabuladores

    with open(output_path, 'w') as outfile:
        for line in cleaned_lines:
            outfile.write(line)

    print(f"Archivo procesado y guardado en {output_path}")
