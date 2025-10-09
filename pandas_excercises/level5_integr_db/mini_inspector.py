import sqlite3

def mostrar_tablas_y_columnas(nombre_db):
    with sqlite3.connect(nombre_db) as conexion:
        cursor = conexion.cursor()

        # Mostrar todas las tablas
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tablas = cursor.fetchall()
        print("🗂️ Tablas encontradas:")
        for tabla in tablas:
            nombre_tabla = tabla[0]
            print(f"\n📌 Tabla: {nombre_tabla}")

            # Mostrar columnas de la tabla
            cursor.execute(f"PRAGMA table_info({nombre_tabla})")
            columnas = cursor.fetchall()
            print("   Columnas:")
            for col in columnas:
                cid, nombre, tipo, notnull, default, pk = col
                print(f"     - {nombre} ({tipo}){' [PK]' if pk else ''}{' NOT NULL' if notnull else ''}")

            # Mostrar SQL de creación
            cursor.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name=?", (nombre_tabla,))
            sql = cursor.fetchone()[0]
            print("   SQL de creación:")
            print(f"     {sql}")

# Ejecutar el inspector
mostrar_tablas_y_columnas("clientes.db")
