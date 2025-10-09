import sqlite3
import pandas as pd

# Leer el Excel con Pandas
df = pd.read_excel("clientes.xlsx", sheet_name="Personas")

# Crear conexión SQLite
conn = sqlite3.connect("clientes.db")

# Insertar en la tabla personas
df.to_sql("Personas", conn, if_exists="replace", index=False)


#  Inserción en base SQLite
#  Fuente: clientes.xlsx, hoja 'Personas'
#  Tabla: personas
#  Versión: insercion_sqlite_v1.0.py
