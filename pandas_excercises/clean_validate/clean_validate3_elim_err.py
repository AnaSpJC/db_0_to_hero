# 1. Eliminar los nulos.
# 2. Eliminar los duplicados.
# 3. Exportar el resultado como datos_limpios.csv.
import pandas as pd

data = {
    "Nombre": ["Ana", "Luis", "Luis", None],
    "Edad": [25, 30, 30, None]
}
df = pd.DataFrame(data)

df_sin_nulos = df.dropna()
df_sin_duplicados = df.drop_duplicates()
print(df_sin_nulos)
print(df_sin_duplicados)
# todo limpio antes de exportar
df_limpio = df.dropna().drop_duplicates()
print(df_limpio)
# exportar
df_limpio.to_csv("datos_limpios.csv", index=False)
#   4. Verificar que el archivo se creó correctamente.
df_verificado = pd.read_csv("datos_limpios.csv")
print(df_verificado)
