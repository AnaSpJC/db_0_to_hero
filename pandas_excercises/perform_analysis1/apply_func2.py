# v02 apply_func1: *_ asegurar trazabilidad y evitar fallos silenciosos 
import pandas as pd
# 🔹 Simil Client RAW data
df = pd.DataFrame({
    "Nombre": [" juan", "MARIA ", "peDro", "123", None],
    "Edad": [35, -5, "veinte", 40, None]
})
def limpiar_nombre(nombre):
    if isinstance(nombre, str) and nombre.strip().isalpha():
        return nombre.strip().title()
    else:
        return "Nombre inválido"
    
def validar_edad(edad):
    try:
        edad_int = int(edad)
        return edad_int if edad_int > 0 else None
    except:
        return None
    
df["Nombre_limpio"] = df["Nombre"].apply(limpiar_nombre)
df["Edad_valida"] = df["Edad"].apply(validar_edad)
print(df)
"""🧾 Curatorial documentation (delivery)
🧼 Normalización de nombres
•	Se eliminaron espacios y se capitalizaron nombres válidos.
•	Se detectaron entradas no textuales o numéricas ("123", None) y se etiquetaron como "Nombre inválido".
🧮 Validación de edad
•	Se convirtieron edades a entero.
•	Se descartaron valores negativos, no numéricos o nulos.
📌 Resultado
•	Se generaron dos columnas nuevas: Nombre_limpio y Edad_valida.
•	El DataFrame está listo para análisis o exportación, con trazabilidad de errores.
"""
        