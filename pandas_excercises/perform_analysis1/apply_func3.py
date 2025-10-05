# v03: Versión con LOGGING NARRATIVO: crear una función que no solo limpie NOMBRE,
#  sino que registre qué pasó con cada entrada.
import pandas as pd
# 🔹 Simil Client RAW data
df = pd.DataFrame({
    "Nombre": [" juan", "MARIA ", "peDro", "123", None],
    "Edad": [35, -5, "veinte", 40, None]
})
def limpiar_nombre_con_log(nombre):
    log = {}
    if isinstance(nombre, str):
        nombre_strip = nombre.strip()
        if nombre_strip.isalpha():
            nombre_limpio = nombre_strip.title()
            log["estado"] = "válido"
            log["original"] = nombre_strip
            log["resultado"] = nombre_limpio
        else:
            nombre_limpio = "Nombre inválido"
            log["estado"] = "caracteres no válidos"
            log["original"] = nombre_strip
            log["resultado"] = nombre_limpio
    else:
        nombre_limpio = "Nombre inválido"
        log["estado"] = "no es texto"
        log["original"] = nombre
        log["resultado"] = nombre_limpio
    return nombre_limpio, log
df["Nombre_limpio"], df["Log_nombre"] = zip(*df["Nombre"].apply(limpiar_nombre_con_log))
print(df)
    
