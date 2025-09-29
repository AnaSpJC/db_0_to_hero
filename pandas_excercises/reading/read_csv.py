# Goal: Errores comunes
# Error 1: Separador incorrecto.
# Error 2: Codificación incompatible.
# Error 3: Falta de encabezado.
# Error 4: Encabezado presente pero querés renombrar

import pandas as pd

df = pd.read_csv("csv_datos.csv") #ok
df_separador = pd.read_csv("csv_datos_separador.csv") #Error 1: Separador incorrecto
df_separador_ok = pd.read_csv("csv_datos_separador.csv", sep=";")
df_codificacion = pd.read_csv("csv_datos_codificacion.csv")# Error 2: Codificación incompatible
df_codificacion_ok = pd.read_csv("csv_datos_codificacion.csv", encoding="latin1")
df_sin_encabezado = pd.read_csv("csv_datos_sin_encabezado.csv")#Error 3: Falta de encabezado
df_sin_encabezado_ok = pd.read_csv("csv_datos_sin_encabezado.csv", header=None, names=["Name", "Age", "City"])
df_renombrar = pd.read_csv("csv_datos_renombrar_encab.csv", names=["A", "B", "C"])#Error 4: Encabezado presente pero querés renombrar
df_renombrar_ok1 = pd.read_csv("csv_datos_renombrar_encab.csv", header=0, names=["A", "B", "C"])# reemplaza nombres
df_renombrar_ok2 = pd.read_csv("csv_datos_renombrar_encab.csv", header=None, names=["A", "B", "C"])# conserva todo como datos

print(df)
print(df_separador)
"""
 Nombre;Edad;Ciudad
0  Ana;30;Buenos Aires
1      Luis;25;Córdoba
"""
print(df_separador_ok)
print(df_codificacion)
print(df_codificacion_ok)
"""Nombre  Edad       Ciudad
0   Mara    40      Rosario
1  JosÃ©    35  San MartÃ­n"""
print(df_sin_encabezado)
"""Ana  30 Buenos Aires
0  Luis  25      Córdoba"""
print(df_sin_encabezado_ok)
print(df_renombrar)
""" A     B             C
0  Nombre  Edad        Ciudad
1     Ana    30  Buenos Aires
2    Luis    25       Córdoba"""
print(df_renombrar_ok1)
""" A   B             C
0   Ana  30  Buenos Aires
1  Luis  25       Córdoba"""
print(df_renombrar_ok2)
print("\nInformación técnica de de_renombrar_ok2:")
print(df_renombrar_ok2.info())