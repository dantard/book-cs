import os
import re
import sys


def renombrar_archivos(directorio):
    # Iterar sobre los archivos del directorio
    for nombre_archivo in os.listdir(directorio):
        # Buscar archivos que coincidan con el patrón 'fichero-1.txt', 'fichero-2.txt', etc.
        match = re.match(r'fichero-(\d+)\.txt', nombre_archivo)
        if match:
            # Obtener el número del archivo y formatearlo con 3 dígitos
            numero = match.group(1)
            nuevo_nombre = f'fichero-{int(numero):03d}.txt'
            # Renombrar el archivo
            os.rename(os.path.join(directorio, nombre_archivo), os.path.join(directorio, nuevo_nombre))


def main():
    if len(sys.argv) != 2:
        print("Usage: python renombrar_archivos.py <directorio>")
        sys.exit(1)

    directorio = sys.argv[1]

    if not os.path.isdir(directorio):
        print(f"Error: El directorio '{directorio}' no es válido.")
        sys.exit(1)

    renombrar_archivos(directorio)
    print(f"Archivos renombrados en el directorio: {directorio}")


if __name__ == "__main__":
    main()