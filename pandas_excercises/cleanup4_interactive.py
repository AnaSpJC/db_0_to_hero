# Módulo actualizado con limpieza interactiva
import pandas as pd

# 🔹 Datos simulados
datos = {
    "DNI": ["12345678", "87654321", "11111111", "22222222", "33333333"],
    "Nombre": ["Ana", "Luis", "Mara", "Lucía", "Carlos"],
    "Edad": ["30", "25", "cuarenta", "-5", "130"]  # errores: texto, valores dudosos
}

df = pd.DataFrame(datos)

# 🔧 Función interactiva de limpieza
def limpiar_columna_numerica_interactiva(df, columna, minimo=0, maximo=120):
    columna_aux = columna + "_valida"
    df[columna_aux] = pd.to_numeric(df[columna], errors="coerce")

    # Detectar errores por conversión fallida
    errores_conversion = df[df[columna_aux].isna()]

    # Detectar errores por rango fuera de límites
    errores_rango = df[(df[columna_aux] < minimo) | (df[columna_aux] > maximo)]

    # Combinar ambos tipos de errores
    errores = pd.concat([errores_conversion, errores_rango]).drop_duplicates()

    if not errores.empty:
        print(f"⚠️ Se detectaron {len(errores)} valores inválidos en '{columna}':")
        print(errores[[columna]])

        for idx in errores.index:
            valor_original = df.at[idx, columna]
            nuevo_valor = input(f"🔧 Corregí el valor '{valor_original}' en fila {idx}: ")
            try:
                nuevo_valor_num = int(nuevo_valor)
                if minimo <= nuevo_valor_num <= maximo:
                    df.at[idx, columna_aux] = nuevo_valor_num
                else:
                    print(f"❌ Valor fuera de rango ({minimo}-{maximo}). Se mantiene como NaN.")
                    df.at[idx, columna_aux] = pd.NA
            except ValueError:
                print("❌ Valor no válido. Se mantiene como NaN.")
                df.at[idx, columna_aux] = pd.NA

    df[columna] = df[columna_aux].astype("Int64")
    df = df.drop(columns=[columna_aux])
    return df

# 🧹 Aplicar limpieza interactiva a la columna 'Edad'
df_limpio = limpiar_columna_numerica_interactiva(df, "Edad")

# 📊 Mostrar resultado final
print(df_limpio)
