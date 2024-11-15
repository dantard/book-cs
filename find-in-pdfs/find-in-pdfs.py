import sys
import os
from PyPDF2 import PdfReader


# Función para buscar una palabra en un archivo PDF.
def buscar_palabra_en_pdf(ruta_pdf, palabra):
    try:
        # Cargar el archivo PDF.
        lector = PdfReader(ruta_pdf)
        # Iterar por las páginas del PDF.
        for num_pagina, pagina in enumerate(lector.pages, start=1):
            # Extraer texto y buscar la palabra (ignorando mayúsculas/minúsculas).
            if palabra.lower() in pagina.extract_text().lower():
                return num_pagina
        return None  # Si no se encuentra la palabra.
    except Exception as e:
        print(f"Error al leer {ruta_pdf}: {e}")
        return None


# Función principal.
def main():
    # Verificar que los argumentos sean suficientes.
    if len(sys.argv) < 3:
        print("Uso: python script.py palabra archivo1.pdf archivo2.pdf ...")
        sys.exit(1)

    # La palabra a buscar es el primer argumento.
    palabra = sys.argv[1]
    # Los archivos PDF son los argumentos siguientes.
    archivos_pdf = sys.argv[2:]

    # Iterar sobre cada archivo PDF.
    for pdf in archivos_pdf:
        # Verificar si el archivo existe.
        if not os.path.isfile(pdf):
            print(f"{pdf} no existe o no es un archivo.")
            continue

        # Buscar la palabra en el archivo.
        pagina = buscar_palabra_en_pdf(pdf, palabra)
        if pagina is not None:
            print(f"La palabra '{palabra}' se encontró en '{pdf}' en la página {pagina}.")
        #else:
        #    print(f"La palabra '{palabra}' no se encontró en '{pdf}'.")


# Punto de entrada del programa.
if __name__ == "__main__":
    main()
