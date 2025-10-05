# Fase 2: Limpieza de columnas
## Objetivo: normalizar Nombre y validar Edad con logging
# Fase 3: Derivación de columnas
## Objetivo: crear Mayor, Rango_Etario

import pandas as pd

df = pd.read_csv("../data_raw/personas_sucursales.csv")
# Función con logging para nombre
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
            log["original"] = nombre
            log["resultado"] = nombre_limpio
    else:
        nombre_limpio = "Nombre inválido"
        log["estado"] = "no es texto"
        log["original"] = nombre
        log["resultado"] = nombre_limpio
    return nombre_limpio, log

# Función con logging para Edad
def validar_edad_con_log(edad):
    log = {}
    try:
        edad_int = int(edad)
        if edad_int > 0:
            log["estado"] = "válida"
            resultado = edad_int
        else:
            log["estado"] = "negativa"
            resultado = None
    except:
        log["estado"] = "no convertible"
        resultado = None
    
    log["original"] = edad
    log["resultado"] = resultado
    return resultado, log

# Aplicar funciones
df["Nombre_limpio"], df["Log_nombre"] = zip(*df["Nombre"].apply(limpiar_nombre_con_log))
df["Edad_valida"], df["Log_edad"] = zip(*df["Edad"].apply(validar_edad_con_log))
print(df)

# Columna Mayor
df["Mayor"] = df["Edad_valida"].apply(lambda x: x > 18 if pd.notnull(x) else None)
# Columna Rango_Etario
df["Rango etario"] = pd.cut(
    df["Edad_valida"],
    bins = [0, 18, 30, 45, 100],
    labels= ["Adolescente", "Jóven", "Adulto", "Mayor"],
    right=True
)

# df.to_excel("../data_clean/pers_limpias_sin_filtrar.xlsx", index=False)

# Filtrar registros válidos
df_validos = df[
    (df["Nombre_limpio"] != "Nombre inválido") &
    (df["Edad_valida"].notnull())]

#print(df_validos) # validados pero no limpios
# Seleccionar columnas limpias
df_entrega = df_validos[["Nombre_limpio", "Edad_valida", "Sucursal", "Mayor", "Rango etario"]]

#df_entrega.to_excel("../outputs/personas_limpias.xlsx", index=False)

# Filtrar registros descartados
df_descartados = df[
    (df["Nombre_limpio"] == "Nombre inválido") |
    (df["Edad_valida"].isnull())
]

# Exportar archivo técnico
#df_descartados.to_excel("../outputs/personas_descartadas.xlsx", index=False)

# Crear resumen para cliente no técnico
df_descartes_cliente = df[
    (df["Nombre_limpio"] == "Nombre inválido") |
    (df["Edad_valida"].isnull())
][["Nombre", "Edad"]].copy()

# Agregar motivo de descarte
def motivo(row):
    if row["Edad"] is None or pd.isna(row["Edad"]):
        return "Edad nula"
    try:
        if int(row["Edad"]) <= 0:
            return "Edad negativa"
    except:
        return "Edad no convertible"
    if not isinstance(row["Nombre"], str) or not row["Nombre"].strip().isalpha():
        return "Nombre no alfabético"
    return "Otro"

df_descartes_cliente["Motivo de descarte"] = df_descartes_cliente.apply(motivo, axis=1)

# Exportar
#df_descartes_cliente.to_excel("../outputs/registros_descartados_cliente.xlsx", index=False)


