import pandas as pd

df = pd.read_csv("personas2.csv")

df = df[df["Edad"] <= 100].reset_index(drop=True)

# 🧪 Crear columna categórica 'Rango_Etario'
df["Rango Etario"] = pd.cut(
    df["Edad"],
    bins= [0, 18, 30, 45, 100],
    labels= ["Adolescente", "Jóven", "Adulto", "Mayor"],
    right= True
)
print(df)
# Exportación curada
df.to_excel("personas_rango_etario.xlsx", index=False)