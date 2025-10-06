# Fase 1: Preparación y lectura del archivo
## Objetivo: cargar el archivo, validar estructura y preparar entorno
###10.	Validar columnas esperadas
"""o	¿Están Nombre, Edad, Sucursal?
o	¿Hay nulos?
o	¿Tipos de datos correctos?"""


import pandas as pd

df = pd.read_csv("../data_raw/personas_sucursales.csv")
print(df.head())
print(df.info())