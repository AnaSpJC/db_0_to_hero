import pandas as pd

# Exploración inicial
# Cargamos el archivo original recibido del cliente
df = pd.read_csv("../data_raw/clientes_translog_original.csv")
print(df.head())
print(df.info())

# Limpieza curatorial sobre columnas clave
## Validamos columnas esenciales: Nombre, Edad, Monto
## Usamos máscara booleana para evitar que dropna() elimine registros válidos con nulos en otras columnas
mask_validos = df[["Nombre", "Edad", "Monto"]].notnull().all(axis=1)
df_limpio = df[mask_validos].drop_duplicates(subset=["Nombre", "Edad", "Monto"])
df_limpio["Edad"] = df_limpio["Edad"].astype(int)

# Exportación intermedia
## Conservamos todas las columnas originales para trazabilidad
df_limpio.to_csv("../data_clean/clientes_translog_cleaned.csv", index=False, encoding="utf-8")

# Exportación curatorial final
## Entregamos solo columnas requeridas por cliente
## Formato compatible con Excel en español: sep=";", decimal=","
df_limpio[["Nombre", "Edad", "Monto"]].to_csv(
    "../outputs/clientes_trimestre.csv",
    sep=";", decimal=",", index=False, encoding="utf-8"
)

# Versión: exportador_csv_translog_v1.0.py — 2025-10-06
