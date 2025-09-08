# Profesionalizar función clase3-prac2 incorporando manejo de errores con try y except,
# validaciones de entrada, y mensajes claros para el usuario.
# Asegurar que la edad sea un número entero y que el DNI no esté vacío.

import sqlite3

def dni_existe(nombre_db, dni):
    try:
        with sqlite3.connect("mi_base.db") as conexion:
            return conexion.execute("SELECT 1 FROM personas WHERE dni= ?", (dni,)).fetchone() is not None
    except sqlite3.Error as e:
        print(f"Error al verificar DNI: {e}")
        return False
    
def registrar_persona(nombre_db):
        while True:
            try:
                dni = input("Qué DNI querés ingresar?: ").strip()
                if not dni:
                    print("El DNI no puede estar vacío.")
                    continue
                if dni_existe(nombre_db, dni):
                    print("El DNI ya está registrado.")
                else:
                    nombre = input("Ingresá el nombre: ").strip()
                    if not nombre:
                        print("El nombre no puede estar vacío.")
                        continue
                    try:
                       edad = int(input("Ingresá la edad: "))
                       if edad < 0:
                            print("La edad no puede ser negativa.")
                            continue
                    except ValueError:
                        print("La edad debe ser un número entero.")
                        continue
                    with sqlite3.connect("mi_base.db") as conexion:
                        cursor = conexion.cursor()
                        cursor.execute("INSERT INTO personas VALUES (?, ?, ?)", (dni, nombre, edad))
                        print(f"La persona registrada es {nombre} DNI: {dni}, {edad}")

            except sqlite3.IntegrityError:
                print("El DNI ya existe en la base de datos (clave duplicada).")
            except sqlite3.Error as e:
                print(f"Error al registrar persona: {e}")
            except Exception as e:
                print(f"Error inesperado: {e}")

            while True:
                continuar = input("¿Quéres registrar otra persona? (S/N)").strip().lower()
                if continuar == "s":
                    break
                elif continuar == "n":
                    print("Finalizando registro... Hasta la próxima!")
                    return
                else:
                    print("Respuesta inválida. Ingresá S o N: ")

registrar_persona("mi_base.db")
    