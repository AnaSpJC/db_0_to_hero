# GOAL: Usr 3 métodos de EXPLORACIÓN (df.head(), df.columns, df.info()).
# Si existen datos que deberían ser numéricos, realizar conversión
import pandas as pd

df = pd.read_csv("csv_datos_sin_encabezado.csv", header=None, names=["Nombre", "Edad", "País"])
print("Primeras 2 Filas (5 primeras filas por default):")
print(df.head(2))
print("Nombres de columnas:")
print(df.columns)
print("Información técnica:")
print(df.info())
print(df)
 