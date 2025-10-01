"""
📄 Lectura de archivos JSON con Pandas
🎯 Propósito: importar datos estructurados desde archivos .json
🔧 Herramienta: pd.read_json("archivo.json")
📦 Estructura esperada: lista de diccionarios
🔍 Exploración: df.head(), df.columns, df.info()
🧪 Aplicación: lectura directa de datos tabulares
📌 Observación: estructuras anidadas requieren json_normalize()
"""
import pandas as pd

df = pd.read_json("datos_simulados.json")
print(df.head())
print(df.info())