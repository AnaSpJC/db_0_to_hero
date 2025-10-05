## Aplicación de funciones con `.apply()`
# Se utilizaron funciones lambda y nativas para limpiar texto y validar valores. 
# Este enfoque permite transformar columnas de forma precisa y reproducible.

### EN
#Used lambda and native functions to clean text and validate values. 
# This approach enables precise and reproducible column transformations.
import pandas as pd

# 🔹 Datos simulados
df = pd.DataFrame({
    "Nombre": [" ana ", "LUIS", "mara"],
    "Edad": [30, 25, 40]
})
df["Nombre_limpio"] = df["Nombre"].apply(lambda x: x.strip().title())
df["Edad_valida"] = df["Edad"].apply(lambda x: x > 0)
print(df)
