# ──────────────────────────────────────────────────────────────
# 📦 Módulo: agregacion_exportacion.py
# 🎯 Objetivo: Fase 4 a Fase 6 del flujo curatorial
# - Agregación por sucursal
# - Ordenamiento por edad
# - Exportación curada de entregables
# ──────────────────────────────────────────────────────────────

import pandas as pd

# Leer archivo limpio generado en limpieza_derivacion.py
df = pd.read_excel("../outputs/personas_limpias.xlsx")

# ──────────────────────────────────────────────────────────────
# 🧮 Fase 4: Agregación por sucursal
# Se calcula:
# - Promedio de edad
# - Edad máxima
# - Cantidad de personas por sucursal
# ──────────────────────────────────────────────────────────────

resumen = df.groupby("Sucursal")["Edad_valida"].agg([
    ("Promedio_Edad", "mean"),
    ("Edad_Máxima", "max"),
    ("Cantidad_Personas", "count")
]).reset_index()

# ──────────────────────────────────────────────────────────────
# 📊 Fase 5: Ordenamiento
# Se ordena por edad descendente y se renumera el índice
# ──────────────────────────────────────────────────────────────

df_ordenado = df.sort_values("Edad_valida", ascending=False).reset_index(drop=True)

# ──────────────────────────────────────────────────────────────
# 📦 Fase 6: Exportación curatorial
# Se generan los archivos finales para entrega
# ──────────────────────────────────────────────────────────────

df_ordenado.to_excel("../outputs/personas_limpias.xlsx", index=False)
resumen.to_excel("../outputs/resumen_sucursal.xlsx", index=False)

# 🧾 Observación:
# Este módulo no modifica datos, solo resume, ordena y exporta.
# La limpieza y derivación ya fueron realizadas en el módulo anterior.
# El archivo `personas_limpias.xlsx` fue actualizado en la Fase 5 con ordenamiento descendente por edad.
# La versión anterior sin ordenar fue reemplazada.

