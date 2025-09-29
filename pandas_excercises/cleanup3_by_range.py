# Módulo actualizado con limpieza por rango
import pandas as pd

# 🔹 Datos simulados
datos = {
    "DNI": ["12345678", "87654321", "11111111", "22222222", "33333333"],
    "Nombre": ["Ana", "Luis", "Mara", "Lucía", "Carlos"],
    "Edad": ["30", "25", "cuarenta", "-5", "130"]  # errores: texto, fuera de rango
}

df = pd.DataFrame(datos)

# 🔧 Función general con validación por rango
def limpiar_columna_numerica(df, columna, minimo=None, maximo=None):
    columna_aux = columna + "_valida"
    df[columna_aux] = pd.to_numeric(df[columna], errors="coerce")
    df = df.dropna(subset=[columna_aux])

    if minimo is not None:
        df = df[df[columna_aux] >= minimo]
    if maximo is not None:
        df = df[df[columna_aux] <= maximo]

    df[columna] = df[columna_aux].astype(int)
    df = df.drop(columns=[columna_aux])
    return df

# 🧹 Aplicar limpieza a la columna 'Edad' con rango válido
df_limpio = limpiar_columna_numerica(df, "Edad", minimo=1, maximo=120)

# 📊 Mostrar resultado
print(df_limpio)
