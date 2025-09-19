import os
import sqlite3
import csv
import json

# 🔹 1. Conexión a la base de datos SQLite
def conectar_db(nombre_db="mi_base.db"):
    # Verifica si el archivo existe antes de intentar conectarse
    if not os.path.exists(nombre_db):
        print(f"⚠️ El archivo '{nombre_db}' no existe.")
        return None
    try:
        # Establece la conexión con la base
        conn = sqlite3.connect(nombre_db)
        print(f"✅ Conexión exitosa a la base '{nombre_db}'")
        return conn
    except sqlite3.Error as e:
        print(f"❌ Error al conectar con la base de datos: {e}")
        return None

# 🔹 2. Validación de datos individuales
def validar_persona(dni, nombre, edad):
    # Verifica que el DNI sea numérico
    if not dni.isdigit():
        return False
    # Verifica que la edad sea numérica y positiva
    if not edad.isdigit() or int(edad) <= 0:
        return False
    # Verifica que el nombre no esté vacío
    if not nombre.strip():
        return False
    return True

# 🔹 3. Validación de nombre de archivo
def validar_nombre_archivo(nombre, extension):
    # Verifica que el nombre no esté vacío y tenga la extensión correcta
    if not nombre.strip():
        print("❌ El nombre del archivo no puede estar vacío.")
        return False
    if not nombre.lower().endswith(extension):
        print(f"❌ El archivo debe tener la extensión '{extension}'")
        return False
    return True

# 🔹 4. Exportar datos a archivo CSV
def exportar_a_csv(conn, nombre_archivo="personas.csv", incluir_encabezado=True):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT dni, nombre, edad FROM personas")
        datos = cursor.fetchall()

        # Abre el archivo CSV en modo escritura
        with open(nombre_archivo, mode="w", newline='', encoding="utf-8") as archivo_csv:
            escritor = csv.writer(archivo_csv)
            # Escribe encabezado si está habilitado
            if incluir_encabezado:
                escritor.writerow(["DNI", "Nombre", "Edad"])
            # Escribe todas las filas
            escritor.writerows(datos)

        print(f"✅ Datos exportados correctamente a '{nombre_archivo}'")
    except Exception as e:
        print(f"❌ Error al exportar a CSV: {e}")

# 🔹 5. Exportar datos a archivo JSON
def exportar_a_json(conn, nombre_archivo="personas.json"):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT dni, nombre, edad FROM personas")
        datos = cursor.fetchall()

        # Convierte cada fila en un diccionario
        lista_dicts = []
        for fila in datos:
            dni, nombre, edad = fila
            persona = {"dni": dni, "nombre": nombre, "edad": edad}
            lista_dicts.append(persona)

        # Guarda la lista de diccionarios en formato JSON
        with open(nombre_archivo, mode="w", encoding="utf-8") as archivo_json:
            json.dump(lista_dicts, archivo_json, indent=4, ensure_ascii=False)

        print(f"✅ Datos exportados correctamente a '{nombre_archivo}'")
    except Exception as e:
        print(f"❌ Error al exportar a JSON: {e}")

# 🔹 6. Importar datos desde archivo CSV
def importar_desde_csv(conn, nombre_archivo="personas.csv", sobrescribir=False):
    try:
        cursor = conn.cursor()

        # Si sobrescribir está activado, vacía la tabla antes de importar
        if sobrescribir:
            cursor.execute("DELETE FROM personas")
            print("🧹 Tabla 'personas' vaciada antes de importar")

        # Abre el archivo CSV en modo lectura
        with open(nombre_archivo, mode="r", encoding="utf-8") as archivo_csv:
            lector = csv.DictReader(archivo_csv)
            registros_insertados = 0

            for fila in lector:
                dni = fila["DNI"]
                nombre = fila["Nombre"]
                edad = fila["Edad"]

                # Valida los datos antes de insertar
                if not validar_persona(dni, nombre, edad):
                    print(f"⚠️ Registro inválido: {fila}")
                    continue

                # Verifica si el DNI ya existe en la base
                cursor.execute("SELECT COUNT(*) FROM personas WHERE dni = ?", (dni,))
                if cursor.fetchone()[0] > 0:
                    print(f"🔁 DNI duplicado, se omite: {dni}")
                    continue

                # Inserta el registro en la base
                cursor.execute("INSERT INTO personas (dni, nombre, edad) VALUES (?, ?, ?)", (dni, nombre, edad))
                registros_insertados += 1

            conn.commit()
            print(f"✅ Se importaron {registros_insertados} registros desde '{nombre_archivo}'")
    except Exception as e:
        print(f"❌ Error al importar desde CSV: {e}")

# 🔹 7. Menú interactivo para ejecutar funciones
if __name__ == "__main__":
    conn = conectar_db()
    if conn:
        print("\n📋 Menú de opciones:")
        print("1. Exportar a CSV")
        print("2. Exportar a JSON")
        print("3. Importar desde CSV")
        opcion = input("Elegí una opción (1/2/3): ")

        if opcion == "1":
            nombre = input("📁 Ingresá el nombre del archivo CSV (ej: agenda.csv): ")
            if validar_nombre_archivo(nombre, ".csv"):
                exportar_a_csv(conn, nombre_archivo=nombre)

        elif opcion == "2":
            nombre = input("📁 Ingresá el nombre del archivo JSON (ej: personas.json): ")
            if validar_nombre_archivo(nombre, ".json"):
                exportar_a_json(conn, nombre_archivo=nombre)

        elif opcion == "3":
            nombre = input("📁 Ingresá el nombre del archivo CSV a importar (ej: agenda.csv): ")
            if validar_nombre_archivo(nombre, ".csv"):
                sobrescribir = input("¿Querés sobrescribir los datos existentes? (s/n): ").lower() == "s"
                importar_desde_csv(conn, nombre_archivo=nombre, sobrescribir=sobrescribir)

        else:
            print("❌ Opción inválida")

        conn.close()
