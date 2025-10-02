import pandas as pd

df = pd.read_csv("personas2.csv")

df = df[df["Edad"] <= 100].reset_index(drop=True)

# 🧪 Nueva columna: validación de mayoría de edad
df["Mayor"] = df["Edad"] >= 18
print(df) # muestra nueva col con True si >=18 o False si no

# 📊 Filtrar solo mayores de edad
df_mayor = df[df["Mayor"] == True].reset_index(drop=True)
print(df_mayor)

# Exportación curada
df_mayor.to_excel("personas_mayores.xlsx", index=False)

# 🧱 Bloque técnico para portfolio
# 🧪 Nueva columna 'Mayor': se considera mayor si Edad > 18
# 🔍 Filtro aplicado para seleccionar únicamente personas mayores
# 📦 Exportación curatorial a Excel para entrega profesional