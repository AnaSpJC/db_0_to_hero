# Clase 1 – Primer contacto con SQLite
# Objetivo: Crear tu primera base de datos y entender la conexión. 
# Prueba extra: Cambiá el nombre del archivo en connect() y fijate que se crea otro archivo nuevo

import sqlite3

conexion = sqlite3.connect("mi_base_prueba_extra.db")
print("Base creada y conectada con éxito")

conexion.close()
