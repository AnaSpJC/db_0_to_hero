# 🔧 Conversión de tipos: se ajustan columnas para análisis, exportación y consistencia
# 🔍 Edad → int, Altura → float, Nombre → str, Nacimiento → datetime

import pandas as pd

data = {
    "Nombre": ["Ana", "Luis", "María"],
    "Edad": ["25", "30", "40"],
    "Altura": ["1.65", "1.80", "1.75"],
    "Nacimiento": ["1998-05-12", "1990-11-03", "1985-07-22"]
}
df = pd.DataFrame(data)

# 🔧 Conversión de tipos
df["Edad"] = df["Edad"].astype(int)         # 🔧 int: para cálculos o bases de datos
df["Altura"] = df["Altura"].astype(float)   # 🔧 float: para promedios, estadísticas
df["Nombre"] = df["Nombre"].astype(str)     # 🔧 str: para impresión o exportación
df["Nacimiento"] = pd.to_datetime(df["Nacimiento"])  # 🕒 datetime: para análisis de fechas

# 📋 Verificación
print(df.dtypes)
# Exportación segura
df.to_csv("datos_convertidos.csv", index=False)
