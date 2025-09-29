# GOAL: detectar errores de tipo (como "cuarenta" en vez de 40) y entender cómo Pandas responde
import pandas as pd

# Diccionario de datos
datos = {
    "DNI": ["12345678", "87654321", "11111111"],
    "Nombre": ["Ana", "Luis", "Mara"],
    "Edad": ["30", "25", "cuarenta"]  # intencionalmente incorrecto
}

# 🔹 Crear el DataFrame
df = pd.DataFrame(datos)
# 🔍 Mostrar tabla original
print("\nDataFrame original:")
print(df)
# 🔎 Validación: intentar convertir 'Edad' a entero
print("\n🔍 Intentando convertir 'Edad' a entero:")
try:
    df["Edad"] = df["Edad"].astype(int)
    print("Conversión Exitosa")
    print(df)
except ValueError as e:
    print(f"Error de conversión: {e}")

