# Ejercicio completo – Ordenamiento y detección de outliers
# Objetivo
#•	Ordenar los datos por edad
#•	Detectar posibles outliers
#•	Exportar el resultado ordenado
import pandas as pd

# 📥 Carga del archivo
df = pd.read_csv("personas2.csv")

# 📊 Ordenamiento por edad descendente
df_ordenado = df.sort_values("Edad", ascending=False).reset_index(drop=True)

# 🔍 Detección visual de outliers
print(df_ordenado.head())   # Ver los más altos
print(df_ordenado.tail())   # Ver los más bajos

# 📊 Estadísticas para validar extremos
print(df["Edad"].describe())

# 🔍 Eliminación de outliers: se descartan edades mayores a 100 años.
# 🔍 Filtro de outliers: se descartan edades mayores a 100
# 📊 Ordenamiento por edad descendente
# 🧼 Renumeración de índice para entrega limpia
df_ordenado_filt = df_ordenado[df_ordenado["Edad"] <= 100].reset_index(drop=True)
print(df_ordenado_filt)

# 📦 Exportación ordenada
df_ordenado_filt.to_excel("personas2_ordenadas.xlsx", index=False)

# 🧱 Curatorial blocks
# 📊 Ordenamiento por edad para detectar extremos
# 🔍 Validación de outliers con describe() y revisión visual
# 📦 Exportación curatorial para entrega profesional

