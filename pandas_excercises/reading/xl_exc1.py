# 1. Una vez generado el archivo datos_simulados.xlsx cargar las hojas que contenga
#  y explorar cada data frame.
# 2. Cargar todas las hojas juntas

import pandas as pd

# Personas sheet
df_personas = pd.read_excel("datos_simulados.xlsx", sheet_name="Personas")
# Ciudades sheet
df_ciudades = pd.read_excel("datos_simulados.xlsx", sheet_name="Ciudades")
# Explore each data frame
print(df_personas.head(2)) # .head() => 5 first rows
print(df_personas.info())
print(df_ciudades.head())
print(df_ciudades.info())
"""
📄 Lectura de múltiples hojas desde archivo Excel
🎯 Propósito: importar todas las hojas en un solo paso
🔧 Herramienta: pd.read_excel(sheet_name=None)
📦 Resultado: diccionario con nombre de hoja → DataFrame
🔁 Loop: for nombre, hoja in hojas.items()
    - nombre: nombre de la hoja
    - hoja: DataFrame con los datos
🧪 Aplicación: exploración, limpieza, documentación hoja por hoja
"""
hojas_juntas = pd.read_excel("datos_simulados.xlsx", sheet_name=None)
for nombre_hoja, data_frame in hojas_juntas.items():
    print(f"Nombre de la hoja: {nombre_hoja}")
    print(data_frame.head())
