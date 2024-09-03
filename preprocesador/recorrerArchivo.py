import os


def recorrer_archivo(file_path: str):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"El archivo {file_path} no existe.")

    with open(file_path, 'r') as file:
        while (char := file.read(1)):
            print(char, end='')

    print("\nLectura del archivo completa.")
