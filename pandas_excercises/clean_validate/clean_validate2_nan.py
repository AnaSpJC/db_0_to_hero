# 1. Detectar cuántos nulos hay por columna. .isnull().sum()
# 2. Mostrar solo las filas que tienen al menos un nulo.
# 3. Mostrar solo las filas completas (sin nulos). .notnull()
import pandas as pd
data = {
    "Nombre": ["Ana", "Luis", None, "Pedro"],
    "Edad": [25, None, 30, 40]
}
df = pd.DataFrame(data)
nulos_por_columna = df.isnull().sum()
filas_1_nulo = df[df.isnull().any(axis=1)]
cols_1_nulo = df.isnull().any(axis=0) # si alguna columna tiene nulos
cols_con_nulos = df.columns[df.isnull().any(axis=0)] # si alguna columna tiene nulos
filas_completas = df[df.notnull().all(axis=1)]
print(nulos_por_columna)
print(filas_1_nulo)
print(cols_1_nulo)
print(cols_con_nulos)
print(filas_completas)