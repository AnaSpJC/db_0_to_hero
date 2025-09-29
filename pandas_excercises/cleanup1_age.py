# 🔍 Limpieza automática de 'Edad'

import pandas as pd

# 🔹 Datos simulados
datos = {
    "DNI": ["12345678", "87654321", "11111111"],
    "Nombre": ["Ana", "Luis", "Mara"],
    "Edad": ["30", "25", "cuarenta"]
}
df = pd.DataFrame(datos)

# 🔍 Limpieza automática de 'Edad'
df["Edad_valida"] = pd.to_numeric(df["Edad"], errors="coerce")  
df = df.dropna(subset=["Edad_valida"])
df["Edad"] = df["Edad_valida"].astype(int)                      
df = df.drop(columns=["Edad_valida"])

# 📊 Resultado limpio
print(df)
