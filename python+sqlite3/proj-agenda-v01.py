# Clase 8 – Proyecto integrador ==> Objetivo: Unir todo en un pequeño sistema de gestión.
# Crea un archivo agenda.py que:
# 1.    Muestre un menú con opciones: Agregar, Buscar, Modificar, Eliminar, Listar todos.
# 2.    Use funciones para cada acción.
# 3.    Mantenga la conexión usando with.
# 💡 Prueba extra: Manejo de errores y excepciones. Validaciones para evitar DNIs duplicados y edad negativa.

import sqlite3
from advancedsearch import buscar_persona_avanzada

def dni_existe(dni):
    try:
        with sqlite3.connect("mi_base.db") as conexion:
            return conexion.execute("SELECT 1 FROM personas WHERE dni = ?", (dni,)).fetchone() is not None
    except sqlite3.Error as e:
        print(f"Error al verificar DNI: {e}")
        return False

def buscar_por_campo(campo, patron):
    try:
        with sqlite3.connect("mi_base.db") as conexion:
            cursor = conexion.cursor()
            query = f"SELECT * FROM personas WHERE {campo} LIKE ?"
            parametro = f"%{patron}%"
            return cursor.execute(query, (parametro,)).fetchall()
    except sqlite3.Error as e:
        print(f"Error en la búsqueda (DB): {e}")
        return []
    except Exception as e:
        print(f"Error inesperado: {e}")
        return []

def seleccionar_persona():
    print("\n=== SELECCIÓN DE PERSONA ===")
    print("1. Buscar por DNI")
    print("2. Buscar por nombre")
    opcion = input("Elegí una opción (1 o 2): ").strip()

    if opcion == "1":
        patron = input("Ingresá DNI completo o parte: ").strip()
        if not patron.isdigit():
            print("El DNI debe contener sólo números.")
            return None
        resultados = buscar_por_campo("dni", patron)
    elif opcion == "2":
        patron = input("Ingresá nombre completo o parte: ").strip()
        if not patron:
            print("El nombre no puede estar vacío.")
            return None
        resultados = buscar_por_campo("nombre", patron)
    else:
        print("Opción inválida.")
        return None

    if not resultados:
        print("No se encontraron coincidencias.")
        return None

    print("\nPersonas encontradas:")
    for i, persona in enumerate(resultados, start=1):
        print(f"{i}. DNI: {persona[0]} | Nombre: {persona[1]} | Edad: {persona[2]}")

    indice = input("Ingresá el número de la persona: ").strip()
    if not indice.isdigit() or not (1 <= int(indice) <= len(resultados)):
        print("Selección inválida.")
        return None

    return resultados[int(indice) - 1]

def agregar_persona():
    while True:
        try:
            dni = input("Ingresá DNI: ").strip()
            if not dni or not dni.isdigit():
                print("El DNI debe ser numérico y no vacío.")
                continue
            if dni_existe(dni):
                print("Este DNI ya está registrado.")
                continue

            nombre = input("Ingresá nombre: ").strip().lower()
            if not nombre:
                print("El nombre no puede estar vacío.")
                continue

            edad = input("Ingresá edad: ").strip()
            if not edad.isdigit() or int(edad) <= 0:
                print("La edad debe ser un número positivo.")
                continue

            with sqlite3.connect("mi_base.db") as conexion:
                conexion.execute("INSERT INTO personas VALUES (?, ?, ?)", (dni, nombre, int(edad)))
                print(f"✅ Registraste a: {nombre}, DNI: {dni}, Edad: {edad} años")
        except sqlite3.Error as e:
            print(f"Error al registrar persona: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")

        continuar = input("¿Registrar otra persona? (S/N): ").strip().lower()
        if continuar != "s":
            print("Finalizando registro... ¡Hasta la próxima!")
            return

def buscar_persona():
    while True:
        persona = seleccionar_persona()
        if persona:
            print(f"\n🔍 Resultado: DNI: {persona[0]} | Nombre: {persona[1]} | Edad: {persona[2]}")
        continuar = input("¿Buscar otra persona? (S/N): ").strip().lower()
        if continuar != "s":
            print("Finalizando búsqueda.")
            return

def modificar_persona():
    persona = seleccionar_persona()
    if not persona:
        return

    print(f"\nSeleccionaste: DNI: {persona[0]} | Nombre: {persona[1]} | Edad: {persona[2]}")
    nuevo_nombre = input("Nuevo nombre (dejar vacío para mantener): ").strip().lower()
    nueva_edad = input("Nueva edad (dejar vacío para mantener): ").strip()

    nombre_final = nuevo_nombre if nuevo_nombre else persona[1]
    edad_final = persona[2]
    if nueva_edad:
        if nueva_edad.isdigit() and int(nueva_edad) > 0:
            edad_final = int(nueva_edad)
        else:
            print("Edad inválida.")
            return

    confirmar = input("¿Aplicar cambios? (S/N): ").strip().lower()
    if confirmar != "s":
        print("Cambios cancelados.")
        return

    try:
        with sqlite3.connect("mi_base.db") as conexion:
            cursor = conexion.cursor()
            cursor.execute("UPDATE personas SET nombre = ?, edad = ? WHERE dni = ?", (nombre_final, edad_final, persona[0]))
            print("✅ Persona modificada con éxito.")
    except sqlite3.Error as e:
        print(f"Error al modificar persona: {e}")

def eliminar_personas():
    persona = seleccionar_persona()
    if not persona:
        return

    confirmar = input(f"¿Eliminar a {persona[1]} (DNI: {persona[0]})? (S/N): ").strip().lower()
    if confirmar != "s":
        print("Eliminación cancelada.")
        return

    try:
        with sqlite3.connect("mi_base.db") as conexion:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM personas WHERE dni = ?", (persona[0],))
            print("🗑️ Persona eliminada con éxito.")
    except sqlite3.Error as e:
        print(f"Error al eliminar persona: {e}")

def lista_personas():
    try:
        with sqlite3.connect("mi_base.db") as conexion:
            cursor = conexion.cursor()
            personas = cursor.execute("SELECT * FROM personas ORDER BY nombre").fetchall()
            print("\n📋 Lista de personas:")
            for persona in personas:
                print(f"DNI: {persona[0]} | Nombre: {persona[1]} | Edad: {persona[2]}")
    except sqlite3.Error as e:
        print(f"Error al listar personas: {e}")

def salir():
    print("👋 Gracias por usar la agenda. ¡Hasta pronto!")

def menu():
    while True:
        print("\n" + "="*30)
        print("           AGENDA")
        print("="*30)
        print("1. Agregar persona")
        print("2. Buscar persona simple")
        print("3. Buscar persona avanzada")
        print("4. Modificar persona")
        print("5. Eliminar persona")
        print("6. Listar todas")
        print("7. Salir")

        try:
            opcion = int(input("Elegí la opción: "))
            match opcion:
                case 1: agregar_persona()
                case 2: buscar_persona()
                case 3: buscar_persona_avanzada()
                case 4: modificar_persona()
                case 5: eliminar_personas()
                case 6: lista_personas()
                case 7: salir(); break
                case _: print("Opción inválida.")
        except ValueError:
            print("La opción debe ser un número entero.")

if __name__ == "__main__":
    menu()
