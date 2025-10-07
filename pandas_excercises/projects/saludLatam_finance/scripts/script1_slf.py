"""
Script de procesamiento curatorial para el caso SaludDigital LATAM_Finanzas.

Cliente: Dirección de Finanzas de una red de clínicas privadas
Fecha: Octubre 2025
Objetivo: Generar un archivo Excel con dos hojas:
    - Resumen mensual de pacientes ingresados (ordenado por fecha, con columna de mes)
    - Detalle de montos facturados por edad (agrupado, con totales)

Flujo:
1. Carga de archivo original desde carpeta /data_raw
2. Limpieza curatorial: eliminación de duplicados y nulos, conversión de tipos
3. Validación de estructura y consistencia
4. Generación de hoja resumen con columna auxiliar de mes
5. Generación de hoja de montos por edad
6. Exportación profesional con formato usando XlsxWriter

Formato de entrega:
- Excel con dos hojas: "Resumen_Pacientes" y "Montos_por_Edad"
- Fechas en formato LATAM (dd/mm/yyyy)
- Encabezados en negrita, texto centrado, columnas ajustadas

Autor: Ana Sposito
Versión: 1.0
"""

import pandas as pd

# Cargar el archivo original
data = "../data_raw/pacientes_julio-sep2025.csv"
df = pd.read_csv(data)

# Eliminar duplicados y filas con valores nulos
df = df.drop_duplicates().dropna()

# Asegurar tipo de dato correcto en 'Monto' y fecha en formato
df["Monto"] = df["Monto"].astype(float)
df["Fecha_Ingreso"] = pd.to_datetime(df["Fecha_Ingreso"])

# Validaciones post-limpieza
assert df.isnull().sum().sum() == 0, "Hay valores nulos después de la limpieza"
assert df.dtypes["Monto"] == "float64", "La columna 'Monto' sigue sin ser numérica"

# Crear hoja de resumen con columnas relevantes
df_resumen = df[["ID", "Nombre", "Edad", "Fecha_Ingreso", "Cobertura"]].copy()
df_resumen["Mes_Ingreso"] = df_resumen["Fecha_Ingreso"].dt.strftime("%B")
df_resumen = df_resumen.sort_values("Fecha_Ingreso")
df_resumen["Fecha_Ingreso"] = df_resumen["Fecha_Ingreso"].dt.strftime("%d/%m/%Y")

# Exportación intermedia para revisión
df_resumen.to_csv("../data_clean/resumen_intermedio.csv", index=False)

# Crear hoja de montos facturados por edad
df_montos = df.groupby("Edad").agg(
    Cantidad_Pacientes=("ID", "count"),
    Monto_Total=("Monto", "sum")
).reset_index()

# Validaciones finales
assert df_resumen.isnull().sum().sum() == 0, "Resumen de pacientes contiene nulos"
assert df_montos.isnull().sum().sum() == 0, "Montos por edad contiene nulos"

# Exportar ambas hojas con formato profesional usando xlsxwriter
output_path = "../outputs/informe_finanzas_octubre2025.xlsx"
with pd.ExcelWriter(output_path, engine="xlsxwriter") as writer:
    # Exportar hojas
    df_resumen.to_excel(writer, sheet_name="Resumen_Pacientes", index=False)
    df_montos.to_excel(writer, sheet_name="Montos_por_Edad", index=False)

    # Acceder al workbook y worksheets
    workbook = writer.book
    ws_resumen = writer.sheets["Resumen_Pacientes"]
    ws_montos = writer.sheets["Montos_por_Edad"]

    # Formatos curados
    formato_encabezado = workbook.add_format({"bold": True, "align": "center", "bg_color": "#DDEBF7"})
    formato_centrado = workbook.add_format({"align": "center"})
    formato_fecha = workbook.add_format({"num_format": "dd/mm/yyyy", "align": "center"})

    # Aplicar formato a encabezados
    for col_num, value in enumerate(df_resumen.columns):
        ws_resumen.write(0, col_num, value, formato_encabezado)
        ws_resumen.set_column(col_num, col_num, 18, formato_centrado)

    for col_num, value in enumerate(df_montos.columns):
        ws_montos.write(0, col_num, value, formato_encabezado)
        ws_montos.set_column(col_num, col_num, 20, formato_centrado)
