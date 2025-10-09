# 📦 Limpieza curatorial y exportación a SQLite
# 🔍 Fuente: clientes_original_raw.xlsx
# 🔍 Validaciones aplicadas:
#     - Edad > 0
#     - Email válido (presente, con @, formato correcto)
#     - Nombre y Ciudad presentes
#     - Duplicados eliminados
# 🧱 Tabla destino: personas_validas
# 🧱 Base: clientes.db
# 🧱 Versión: validacion_sqlite_v1.0.py

import pandas as pd
import sqlite3
import re

# 🧪 Paso 1: Leer archivo Excel
df_raw = pd.read_excel("clientes_original_raw.xlsx")

# 🧪 Paso 2: Validar emails
def email_valido(email):
    if pd.isnull(email):
        return False
    if "@" not in email:
        return False
    if email.endswith("."):
        return False
    patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(patron, email))

# 🧪 Paso 3: Aplicar validaciones curadas
df_validado = df_raw.copy()
df_validado = df_validado[df_validado["Edad"] > 0]
df_validado = df_validado.dropna(subset=["Nombre", "Ciudad"])
df_validado = df_validado[df_validado["Email"].apply(email_valido)]
df_validado = df_validado.drop_duplicates()

# 🧪 Paso 4: Exportar a SQLite
conn = sqlite3.connect("clientes.db")
df_validado.to_sql("personas_validas", conn, if_exists="append", index=False)

# 🧱 Log de exportación
print(f"Registros exportados: {df_validado.shape[0]}")
