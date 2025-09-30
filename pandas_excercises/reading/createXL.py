import pandas as pd

# 🔹 Datos para hoja "Personas"
personas = pd.DataFrame({
    "Nombre": ["Ana", "Luis", "Mara"],
    "Edad": [30, 25, 40],
    "Ciudad": ["Buenos Aires", "Córdoba", "Rosario"]
})

# 🔹 Datos para hoja "Ciudades"
ciudades = pd.DataFrame({
    "Ciudad": ["Buenos Aires", "Córdoba", "Rosario"],
    "Provincia": ["Buenos Aires", "Córdoba", "Santa Fe"],
    "Habitantes": [3000000, 1400000, 1200000]
})

# 📝 Crear archivo Excel con dos hojas
with pd.ExcelWriter("datos_simulados.xlsx") as writer:
    personas.to_excel(writer, sheet_name="Personas", index=False)
    ciudades.to_excel(writer, sheet_name="Ciudades", index=False)
