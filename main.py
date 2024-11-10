import sqlite3
import random
from random import randint

def main():
    NUM_ALUMNOS = 5

    from numpy.lib.function_base import insert

    random.seed(9001)

    def cursor_to_latex(query, name, text):
        # Fetch all rows from the cursor

        cursor.execute(query)
        rows = cursor.fetchall()
        if not rows:
            return "No data to display."

        # Get column names
        column_names = [description[0] for description in cursor.description]
        column_names = [ x.replace("_", "\_") for x in column_names]

        # Start the LaTeX table
        latex_table ='\\begin{center}\n'
        latex_table += "\\begin{tabular}{|" + " | ".join(["c"] * len(column_names)) + "|}\n"
        latex_table += "\\hline\n"

        # Add column names
        latex_table += " & ".join(column_names) + " \\\\\n\\hline\n"

        # Add rows
        for row in rows:
            latex_table += " & ".join(str(item) for item in row) + " \\\\\n\\hline\n"

        # End the LaTeX table
        latex_table += "\\end{tabular}\n"

        latex_table+='\captionof{table}{'+text+'}\n'
        latex_table+='\end{center}\n'

        print(latex_table)
        return latex_table


    # Conexión a la base de datos (o creación si no existe)
    conn = sqlite3.connect('escuela_grande.db')
    cursor = conn.cursor()

    cursor.execute('''DROP TABLE IF EXISTS Estudiantes2;''')
    cursor.execute('''DROP TABLE IF EXISTS Estudiantes3;''')
    cursor.execute('''DROP TABLE IF EXISTS Asociacion;''')

    # Crear la tabla Estudiantes (nombre y apellido en un solo campo)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Estudiantes (
        Nombre TEXT NOT NULL,
        Curso TEXT NOT NULL
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Estudiantes2 (
        ID_Estudiante INTEGER PRIMARY KEY AUTOINCREMENT,
        Nombre TEXT NOT NULL,
        Apellido TEXT NOT NULL,
        Curso TEXT NOT NULL
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Estudiantes3 (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Nombre TEXT NOT NULL,
        Apellido TEXT NOT NULL
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Asociacion (
        ID_Estudiante INTEGER NOT NULL,
        Curso TEXT NOT NULL
    );
    ''')


    # Crear la tabla Cursos
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Cursos (
        Curso TEXT NOT NULL PRIMARY KEY,
        Profesor TEXT NOT NULL
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Escuela (
        Estudiante TEXT NOT NULL,
        Curso TEXT NOT NULL,
        Profesor TEXT NOT NULL        
    );
    ''')

    # empty the tables
    cursor.execute('''
    DELETE FROM Estudiantes;
    ''')

    cursor.execute('''
    DELETE FROM Estudiantes2;
    ''')

    cursor.execute('''
    DELETE FROM Cursos;
    ''')

    cursor.execute('''
    DELETE FROM Escuela;
    ''')



    # Lista de nombres y apellidos
    nombres = ['Ana', 'Luis', 'Carmen', 'Pedro', 'Juan', 'María', 'Carlos', 'Sofía', 'Daniel', 'Lucía']
    apellidos = ['García', 'Pérez', 'López', 'Martínez', 'Rodríguez', 'Sánchez', 'Ramírez', 'Torres', 'Hernández', 'Morales']
    subjects = [
        ('Matemáticas', 'Prof. García'),
        ('Historia', 'Prof. Pérez'),
        ('Ciencias', 'Prof. López'),
        ('Inglés', 'Prof. Ramírez'),
        ('Informática', 'Prof. Marquez')
    ]


    # Insertar datos en la tabla Estudiantes con nombres y apellidos
    used_names = []
    estudiantes = []
    estudiantes2 = []
    estudiantes3 = []
    asociaciones = []

    id_estudiante = 1
    while len(used_names)  < NUM_ALUMNOS:
        name = f"{random.choice(nombres)} {random.choice(apellidos)}"


        if name in used_names:
            continue
        used_names.append(name)
        estudiantes3.append((id_estudiante, name.split()[0], name.split()[1]))

        # Between 1 and 2 subjects
        how_many = randint(1, 2)
        samples = random.sample(subjects, how_many)
        for s in samples:
            estudiantes.append((name, s[0]))
            estudiantes2.append((name.split()[0], name.split()[1], s[0]))
            asociaciones.append((id_estudiante, s[0]))

        id_estudiante += 1

    cursor.executemany('''INSERT INTO Estudiantes (Nombre, Curso) VALUES (?, ?);''', estudiantes)
    cursor.executemany('''INSERT INTO Estudiantes2 (Nombre, Apellido, Curso) VALUES (?, ?, ?);''', estudiantes2)
    cursor.executemany('''INSERT INTO Estudiantes3 (ID, Nombre, Apellido) VALUES (?, ?, ?);''', estudiantes3)
    cursor.executemany('''INSERT INTO Asociacion (ID_Estudiante, Curso) VALUES (?, ?);''', asociaciones)
    # Insertar datos en la tabla Cursos
    cursor.executemany('''INSERT INTO Cursos (Curso, Profesor) VALUES (?, ?);''', subjects)

    # Guardar los cambios
    conn.commit()

    cursor.execute('''select Nombre, Cursos.Curso, Profesor from Estudiantes, Cursos where Estudiantes.Curso = Cursos.Curso''')

    escuela = cursor.fetchall()

    cursor.executemany('''
    INSERT INTO Escuela (Estudiante, Curso, Profesor) VALUES (?, ?, ?);
    ''', escuela)




    #cursor_to_latex("select Estudiante, Curso from NoNormalizada", 'Inscripciones', 'Tabla de inscripciones')
    #cursor_to_latex("select distinct Curso, Profesor from NoNormalizada", 'Inscripciones', 'Tabla de inscripciones')
    #cursor_to_latex("select * from Estudiantes", 'Inscripciones', 'Tabla Estudiantes')
    #cursor_to_latex("select * from Estudiantes3", 'Estudiante', 'Tabla de Estudiantes (v2)')
    #cursor_to_latex("select * from Asociacion", 'Asociacion', 'Tabla de Asociacion')
    #cursor_to_latex("select * from Cursos", 'Cursos', 'Tabla de Cursos')
    #cursor_to_latex("select * from Asociacion JOIN Estudiantes3 on Asociacion.ID_Estudiante=Estudiantes3.ID JOIN Cursos on Cursos.Curso = Asociacion.Curso","aa","aa")
    #cursor_to_latex("SELECT * FROM Estudiantes2, Cursos", 'Escuela', 'Tabla de Escuela')
    #cursor_to_latex("SELECT * FROM Escuela", 'Escuela', 'Tabla Escuela')
    cursor_to_latex('''SELECT Apellido, Nombre, Profesor
FROM Asociacion
JOIN Estudiantes3 ON Asociacion.ID_Estudiante=Estudiantes3.ID
JOIN Cursos on Cursos.Curso = Asociacion.Curso
WHERE Cursos.Curso='Ciencias' ORDER BY Apellido ASC''', 'Estudiantes', 'Tabla de Estudiantes')
    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()