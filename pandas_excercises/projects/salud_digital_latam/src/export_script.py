import pandas as pd

# 📥 Lectura del archivo original recibido del cliente
df = pd.read_excel("../data_raw/pacientes_saluddigital_original.xlsx")

# 🧼 Limpieza curatorial sobre columnas clave
columnas_clave = ["Nombre", "Edad", "DNI", "Fecha_turno", "Especialidad"]
mask_validos = df[columnas_clave].notnull().all(axis=1)
df_limpio = df[mask_validos].drop_duplicates(subset=columnas_clave)
df_limpio["Edad"] = df_limpio["Edad"].astype(int)

# 📦 Exportación JSON para integración con API
df_limpio[columnas_clave].to_json(
    "../outputs/pacientes_trimestre.json",
    orient="records",
    lines=True,
    force_ascii=False
)

# 📅 Versión: exportador_json_saluddigital_v1.0.py — 2025-10-06
