# Objetivo del ejercicio
#   1.	Leer el archivo externo ventas_sucursales.csv.
#   2.	Agrupar por sucursal y calcular: 
#       o	Total vendido (sum)
#       o	Promedio por venta (mean)
#       o	Cantidad de operaciones (count)
#3.	Exportar el resumen a un archivo Excel llamado resumen_ventas.xlsx.
import pandas as pd

df = pd.read_csv("ventas_sucursales.csv")

resumen = df.groupby("Sucursal")["Monto_Venta"].agg([
    ("Total_Vendido", "sum"),
    ("Promedio_Venta", "mean"),
    ("Cantidad_Operaciones", "count")
])

resumen.to_excel("resumen_ventas.xlsx", index=True)