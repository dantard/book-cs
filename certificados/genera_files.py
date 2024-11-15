import csv

# Plantilla LaTeX para el certificado
latex_template = r"""
\documentclass[a4paper,12pt]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc} 
\usepackage[spanish]{babel}
\usepackage{graphicx}
\usepackage{geometry}
\usepackage{xcolor}
    % Enables proper encoding for accented characters
\usepackage[spanish]{babel}  % Ensures the document uses Spanish language conventions
\usepackage{lmodern}         % Provides the Latin Modern font family
\geometry{top=2cm, bottom=2cm, left=2cm, right=2cm}

\begin{document}

\begin{center}
    \fbox{
        \begin{minipage}[c][18cm][c]{16cm}
            \begin{center}
                \includegraphics[width=8cm]{images/logo.jpg} \\[1cm]
                {\Huge \bfseries \textcolor{blue}{Certificado de Reconocimiento}} \\[1cm]
                {\large Por la presente se certifica que} \\[0.5cm]
                {\LARGE \bfseries {{tratamiento}} {{nombre}} {{apellido}}} \\[0.5cm]
                {\large ha participado exitosamente en el evento} \\[0.5cm]
                {\bfseries ``Conferencia de Ejemplo''} \\[1cm]
                {\large Otorgado el día 15 de noviembre de 2024.} \\[1cm]
                {\large \bfseries Organización Ejemplo} \\[1cm]
                \begin{minipage}{0.4\textwidth}
                    \centering
                    \rule{6cm}{0.4pt}\\
                    Director
                \end{minipage}
                \hfill
                \begin{minipage}{0.4\textwidth}
                    \centering
                    \rule{6cm}{0.4pt}\\
                    Secretario
                \end{minipage}
            \end{center}
        \end{minipage}
    }
\end{center}

\end{document}
"""

# Ruta al archivo CSV
csv_file = "personas.csv"

# Leer el archivo CSV y generar archivos LaTeX
with open(csv_file, mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Obtener los valores de la fila
        tratamiento = row["Tratamiento"]
        nombre = row["Nombre"]
        apellido = row["Apellido"]

        # Rellenar la plantilla con los valores actuales
        latex_content = latex_template.replace("{{tratamiento}}", tratamiento).replace("{{nombre}}", nombre).replace("{{apellido}}", apellido)

        # Crear un archivo .tex para cada persona
        output_file = f"latex/certificado_{nombre}_{apellido}.tex"
        with open(output_file, mode="w", encoding="utf-8") as latex_file:
            latex_file.write(latex_content)

print("Archivos LaTeX generados exitosamente en la carpeta.")
