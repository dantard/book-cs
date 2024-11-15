import os
import sys


def generar_archivos(directorio):
    # Verificar si el directorio existe, si no, crearlo
    if not os.path.exists(directorio):
        os.makedirs(directorio)

    # Crear 50 archivos con nombre 'fichero-X.txt', donde X es el número
    for i in range(1, 51):
        nombre_archivo = f'fichero-{i}.txt'
        ruta_archivo = os.path.join(directorio, nombre_archivo)
        with open(ruta_archivo, 'w') as archivo:
            archivo.write(f'Contenido del archivo {nombre_archivo}\n')

    print(f"Se han generado 50 archivos en: {directorio}")

def main():
    print("Uso: python genera.py <directorio>")
    if len(sys.argv) != 2:
        sys.exit(1)

    generar_archivos(sys.argv[1])

if __name__ == "__main__":
    main()
