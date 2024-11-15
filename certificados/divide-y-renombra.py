import re
import sys

from PyPDF2 import PdfReader, PdfWriter
import os


def divide_y_renombra(pdf_entrada, carpeta_salida):
    """
    Divide un archivo PDF en páginas individuales y guarda cada página como un archivo separado.

    Args:
        pdf_entrada (str): Ruta del archivo PDF de entrada.
        carpeta_salida (str): Carpeta donde se guardarán las páginas divididas.
    """
    # Asegurarse de que la carpeta de salida existe
    os.makedirs(carpeta_salida, exist_ok=True)

    try:
        # Leer el PDF de entrada
        lector = PdfReader(pdf_entrada)
        total_paginas = len(lector.pages)

        # Procesar cada página
        for numero_pagina in range(total_paginas):

            # Crear un writer para la página actual
            escritor = PdfWriter()
            escritor.add_page(lector.pages[numero_pagina])

            #extraer texto
            texto = lector.pages[numero_pagina].extract_text()
            names = re.findall(r'[CD]AC\.\s*(.*)', texto)
            if len(names)  == 1:
                name = names[0]#.replace(" ", "_")
                print(texto)

                # Crear un nombre único para cada archivo de página
                nombre_salida = os.path.join(carpeta_salida, name + ".pdf")
                with open(nombre_salida, "wb") as archivo_salida:
                    escritor.write(archivo_salida)

                print(f"Guardado: {nombre_salida}")
            else:
                print(f"No se encontro nombre en la pagina {numero_pagina} o hay más de uno")

        print(f"Se dividieron correctamente {total_paginas} páginas en {carpeta_salida}.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python script.py archivo_entrada.pdf carpeta_salida")
        sys.exit(1)

    divide_y_renombra(sys.argv[1], sys.argv[2])
