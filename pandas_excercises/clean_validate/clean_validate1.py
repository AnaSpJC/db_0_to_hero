# Filtrado por condición: 1. Filtrar solo las personas con edad mayor a 0.
#   2. Guardar el resultado en un nuevo DataFrame llamado df_filtrado.
#   3. Exportalo a CSV como edades_validas.csv.
#   4. Verificar que el archivo se creó correctamente.

import pandas as pd

data = {
    "Nombre": ["Ana", "Luis", "María", "Pedro"],
    "Edad": [25, -3, 0, 40]
}
df = pd.DataFrame(data)
df_filtrado = df[df["Edad"] > 0]

df_filtrado.to_csv("edades_validadas.csv", index=False)

#   4. Verificar que el archivo se creó correctamente.
df_verificacion = pd.read_csv("edades_validadas.csv")
print(df_verificacion)