# Clase 6 – Modificando datos
# Objetivo: Actualizar registros existentes.
# 💡 Prueba extra: Intentá actualizar un DNI que no existe. ¿Qué pasa?
import sqlite3

with sqlite3.connect("mi_base.db") as conexion:
    cursor = conexion.cursor()
    cursor.execute("UPDATE personas SET edad = ? WHERE dni = ?", (33, '10000003'))
    print("Registro actualizado:")
    cursor.execute("SELECT * FROM personas WHERE dni = ?", ("10000003",))
    for i in cursor.fetchall():
        print(i)