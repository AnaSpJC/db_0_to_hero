# Clase 4 – Consultando datos
# Objetivo: Recuperar información de la base
# Prueba extra: Cambiá el SELECT * por SELECT nombre FROM personas.
import sqlite3

with sqlite3.connect("mi_base.db") as conexion:
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM personas")
    for fila in cursor.fetchall():
        print(fila)
    cursor.execute("SELECT nombre FROM personas")
    for fila in cursor.fetchall():
        print(fila)
