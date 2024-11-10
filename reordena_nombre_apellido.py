import os
import sys

# Función para cambiar el orden de nombre y apellido en los archivos

def cambiar_orden_archivos(directorio):
    # Verificar si el directorio existe
    if not os.path.exists(directorio):
        print(f"El directorio {directorio} no existe.")
        return

    # Obtener una lista de todos los archivos en el directorio
    archivos = os.listdir(directorio)

    # Filtrar solo los archivos .txt
    archivos_txt = [archivo for archivo in archivos if archivo.endswith(".txt")]

    # Cambiar el nombre de cada archivo
    for archivo in archivos_txt:

        # Obtener el nombre completo del archivo sin la extensión
        nombre_completo = archivo.replace(".txt", "")

        # Dividir el nombre del archivo en nombre y apellido
        nombre, apellido = nombre_completo.split("_")

        # Crear el nuevo nombre de archivo con apellido_nombre.txt
        nuevo_nombre = f"{apellido}_{nombre}.txt"

        # Obtener las rutas completas para renombrar el archivo
        ruta_antigua = os.path.join(directorio, archivo)
        ruta_nueva = os.path.join(directorio, nuevo_nombre)

        # Renombrar el archivo
        os.rename(ruta_antigua, ruta_nueva)

        # Imprimir el cambio realizado
        print(f"Renombrado: {archivo} -> {nuevo_nombre}")

# Función principal
if __name__ == "__main__":
    cambiar_orden_archivos(sys.argv[1])