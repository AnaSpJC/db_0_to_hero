# función general limpiar_columna_numerica(df, columna)
# aplicada específicamente para limpiar la columna "Edad".

import pandas as pd

# 🔹 Datos simulados
datos = {
    "DNI": ["12345678", "87654321", "11111111"],
    "Nombre": ["Ana", "Luis", "Mara"],
    "Edad": ["30", "25", "cuarenta"]  # 'cuarenta' es inválido
}

df = pd.DataFrame(datos)

# 🔧 Función general de limpieza numérica
def limpiar_columna_numerica(df, columna):
    columna_aux = columna + "_valida"
    df[columna_aux] = pd.to_numeric(df[columna], errors="coerce")
    df = df.dropna(subset=[columna_aux])
    df[columna] = df[columna_aux].astype(int)
    df = df.drop(columns=[columna_aux])
    return df

# 🧹 Aplicar limpieza a la columna 'Edad'
df_limpio = limpiar_columna_numerica(df, "Edad")

# 📊 Mostrar resultado
print(df_limpio)
