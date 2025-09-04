# Clase 3 – Insertando datos
# Objetivo: Aprender a agregar registros.
# Prueba extra: Intentá insertar otro registro con el mismo DNI. Observá el error y pensá por qué ocurre.
import sqlite3

with sqlite3.connect("mi_base.db") as conexion:
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO personas VALUES (?, ?, ?)", ("12345678", "Ana", 30))
    print("Registro insertado correctamente")


# Prueba extra: Intentá insertar otro registro con el mismo DNI. Observá el error y pensá por qué ocurre.
# sqlite3.IntegrityError: UNIQUE constraint failed: personas.dni 