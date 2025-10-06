# ──────────────────────────────────────────────────────────────
# 🧾 Proyecto: SucursalNet – Flujo curatorial completo
# 📅 Fecha: Octubre 2025
# 👩‍💻 Autora: Ana Sposito
# 📁 Módulo único con todas las fases integradas
# ──────────────────────────────────────────────────────────────

import pandas as pd

# ──────────────────────────────────────────────────────────────
# 🧼 Fase 2 – Limpieza de nombres y edades
# Se aplican funciones con logging para validar y corregir errores
# ──────────────────────────────────────────────────────────────

df = pd.read_csv("../data_raw/personas_sucursales.csv")

def limpiar_nombre_con_log(nombre):
    log = {}
    if isinstance(nombre, str):
        nombre_strip = nombre.strip()
        if nombre_strip.isalpha():
            nombre_limpio = nombre_strip.title()
            log["estado"] = "válido"
        else:
            nombre_limpio = "Nombre inválido"
            log["estado"] = "caracteres no válidos"
    else:
        nombre_limpio = "Nombre inválido"
        log["estado"] = "no es texto"
    log["original"] = nombre
    log["resultado"] = nombre_limpio
    return nombre_limpio, log

def validar_edad_con_log(edad):
    log = {}
    try:
        edad_int = int(edad)
        if edad_int > 0:
            resultado = edad_int
            log["estado"] = "válida"
        else:
            resultado = None
            log["estado"] = "negativa"
    except:
        resultado = None
        log["estado"] = "no convertible"
    log["original"] = edad
    log["resultado"] = resultado
    return resultado, log

df["Nombre_limpio"], df["Log_nombre"] = zip(*df["Nombre"].apply(limpiar_nombre_con_log))
df["Edad_valida"], df["Log_edad"] = zip(*df["Edad"].apply(validar_edad_con_log))

df_validos = df[
    (df["Nombre_limpio"] != "Nombre inválido") &
    (df["Edad_valida"].notnull())
]

# ──────────────────────────────────────────────────────────────
# 🧪 Fase 3 – Derivación de columnas
# Se generan columnas 'Mayor' y 'Rango_Etario' para segmentación
# ──────────────────────────────────────────────────────────────

df_validos["Mayor"] = df_validos["Edad_valida"].apply(lambda x: x > 18 if pd.notnull(x) else None)

df_validos["Rango_Etario"] = pd.cut(
    df_validos["Edad_valida"],
    bins=[0, 18, 30, 45, 100],
    labels=["Adolescente", "Jóven", "Adulto", "Mayor"],
    right=True
)

# ──────────────────────────────────────────────────────────────
# 🧮 Fase 4 – Agregación por sucursal
# Se calcula promedio, máximo y cantidad de personas por sucursal
# ──────────────────────────────────────────────────────────────

resumen = df_validos.groupby("Sucursal")["Edad_valida"].agg([
    ("Promedio_Edad", "mean"),
    ("Edad_Máxima", "max"),
    ("Cantidad_Personas", "count")
]).reset_index()

# ──────────────────────────────────────────────────────────────
# 📊 Fase 5 – Ordenamiento
# Se ordena por edad descendente y se renumera el índice
# ──────────────────────────────────────────────────────────────

df_ordenado = df_validos.sort_values("Edad_valida", ascending=False).reset_index(drop=True)

# ──────────────────────────────────────────────────────────────
# 📦 Fase 6 – Exportación curada
# Se generan los archivos .xlsx para entrega interna
# ──────────────────────────────────────────────────────────────

df_ordenado.to_excel("../outputs/personas_limpias.xlsx", index=False)
resumen.to_excel("../outputs/resumen_sucursal.xlsx", index=False)

# ──────────────────────────────────────────────────────────────
# 📝 Fase 7 – Documentación técnica
# Este script resume todas las fases del flujo curatorial
# Las decisiones están documentadas en README.md (docs/)
# ──────────────────────────────────────────────────────────────
