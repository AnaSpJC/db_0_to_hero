# 🔢 Simulación de archivo con errores / Simulated file with errors
# 🔍 Conversión inicial de Edad a numérico / Initial conversion of Edad to numeric
# 🔍 Filtrado por condición / Conditional filtering
# 🧼 Detección y eliminación de nulos / Detection and removal of nulls
# 🧹 Eliminación de duplicados / Duplicate removal
# 🔧 Conversión final de tipos / Final type conversion
# 📦 Exportación final / Final export
import pandas as pd
data = {
    "Nombre": ["Ana", "Luis", "Luis", None],
    "Edad": ["25", "-3", "30", None]
}
df = pd.DataFrame(data)
df["Edad"] = pd.to_numeric(df["Edad"], errors="coerce")
df = df[df["Edad"] > 0]
df = df.dropna().drop_duplicates()
df["Edad"] = df["Edad"].astype(int)
df["Nombre"] = df["Nombre"].astype(str)
#print(df) ==> Optional Validation before export
df.to_csv("integration_clean_validat.csv", index=False)
