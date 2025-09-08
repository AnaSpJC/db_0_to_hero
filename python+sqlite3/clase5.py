# Clase 5 – Consultas con condiciones
# Objetivo: Filtrar resultados
# Prueba extra: Usá BETWEEN o LIKE para buscar por rango o patrón
import sqlite3

with sqlite3.connect("mi_base.db") as conexion:
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM personas WHERE edad > ?", (10,))
    print("Personas mayores de 10 años:")
    for i in cursor.fetchall():
        print(i)
    print()
    cursor.execute("SELECT dni FROM personas WHERE edad BETWEEN ? AND ?", (30, 40))
    print("DNI de personas entre 30 y 40:")
    for i in cursor.fetchall():
        print(i)
    print()
    cursor.execute("SELECT nombre FROM personas WHERE edad BETWEEN ? AND ?", (20, 29))
    print("Nombre de personas entre 20 y 29:")
    for i in cursor.fetchall():
        print(i)
    cursor.execute("SELECT * FROM personas WHERE nombre LIKE ?", ("A%",))
    print("Personas cuyo nombre empieza con A")
    for i in cursor.fetchall():
        print(i)
    print()
    print("Nombre y edad de personas con '2' en el nombre:")
    cursor.execute("SELECT nombre, edad FROM personas WHERE nombre LIKE ?", ("%2%",))
    for cualquiera in cursor.fetchall():
        print(cualquiera) 
    print()
    print("Nombre y DNI de personas que comienzan con 1caracter, siguen con 'na' en el nombre:")
    cursor.execute("SELECT nombre, dni FROM personas WHERE nombre LIKE ?", ("_na%",))
    for i in cursor.fetchall():
        print(i)

