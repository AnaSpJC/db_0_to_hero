# Clase 2 – Creando tu primera tabla
# Objetivo: Entender qué es una tabla y cómo definirla
# USO DE WITH AS :
# Prueba extra: Cambiá el nombre de la tabla y volvé a ejecutar.
# ¿Qué pasa si quitás IF NOT EXISTS y la tabla ya existe?

import sqlite3

with sqlite3.connect("mi_base.db") as conexion:
  cursor = conexion.cursor()
  cursor.execute("""
    CREATE TABLE IF NOT EXISTS personas(
      dni TEXT PRIMARY KEY,
      nombre TEXT NOT NULL,
      edad INTEGER CHECK(edad > 0)
      )
  """)
  print("Tabla 'personas' creada con éxito")