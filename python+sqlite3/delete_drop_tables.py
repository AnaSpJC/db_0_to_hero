import sqlite3

def borrar_tabla_interactiva(nombre_db):
    with sqlite3.connect(nombre_db) as conexion:
        cursor = conexion.cursor()

        # Mostrar todas las tablas
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tablas = [fila[0] for fila in cursor.fetchall()]

        if not tablas:
            print("⚠️ No hay tablas en la base de datos.")
            return

        print("🗂️ Tablas disponibles:")
        for i, tabla in enumerate(tablas, start=1):
            print(f"  {i}. {tabla}")

        # Elegir tabla
        opcion = input("\n🔍 Escribí el nombre exacto de la tabla que querés borrar: ").strip()

        if opcion not in tablas:
            print(f"❌ La tabla '{opcion}' no existe.")
            return

        # Confirmación
        confirmar = input(f"⚠️ ¿Estás segura que querés borrar la tabla '{opcion}'? Esto eliminará todos sus datos y estructura. (sí/no): ").strip().lower()

        if confirmar == "sí":
            cursor.execute(f"DROP TABLE IF EXISTS {opcion}")
            print(f"✅ Tabla '{opcion}' eliminada.")
        else:
            print("🛑 Operación cancelada. No se borró nada.")

# Ejemplo de uso
borrar_tabla_interactiva("mi_base.db")
