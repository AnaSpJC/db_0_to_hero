# Clase 8 – Proyecto integrador ==> Objetivo: Unir todo en un pequeño sistema de gestión.
# Crea un archivo agenda.py que:
# 1.	Muestre un menú con opciones: Agregar, Buscar, Modificar, Eliminar, Listar todos.
# 2.	Use funciones para cada acción.
# 3.	Mantenga la conexión usando with.
# 💡 Prueba extra: Manejo de errores y excepciones. Agregá validaciones para que no se repitan DNIs y para que la edad sea positiva.

import sqlite3

def dni_existe(dni):
    try:
        with sqlite3.connect("mi_base.db") as conexion:
            return conexion.execute("SELECT 1 FROM personas WHERE dni = ?", (dni,)).fetchone() is not None
    except sqlite3.Error as e:
        print(f"Error al verificar DNI: {e}")
        return False


def agregar_persona():
    while True:
        try:
            dni = input("Ingresá DNI: ").strip()
            if not dni:
                print("El DNI no puede estar vacío.")
                continue
            if not dni.isdigit():
                print("El DNI sólo debe contener números.")
                continue
            if dni_existe(dni):
                print("Este DNI ya está registrado.")
            else:
                nombre = input("Ingresá nombre: ").strip()
                if not nombre:
                    print("El nombre no puede estar vacío.")
                    continue
                try:
                    edad = int(input("Ingresá edad: "))
                    if edad <= 0:
                        print("La edad debe ser un número mayor a 0.")
                        continue
                except ValueError:
                    print("La edad debe ser un número entero.")
                    continue

                with sqlite3.connect("mi_base.db") as conexion:
                    cursor = conexion.cursor()
                    cursor.execute("INSERT INTO personas VALUES (?, ?, ?)", (dni, nombre, edad))
                    print(f"Persona registrada con éxito.\n Registraste a: {nombre}, DNI: {dni}, Edad: {edad} años")
        except sqlite3.IntegrityError:
            print("Error: El DNI ya existe en la base de datos (clave duplicada).")
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

def buscar_persona():
    while True:
        try:
            print("\n===BÚSQUEDA DE PERSONAS===")
            print("1. Buscar por DNI")
            print("2. Buscar por nombre")
            opcion = input("Elegí una opción ( 1 o 2 ): ").strip()

            if opcion == "1":
                patron = input("Ingresá DNI completo o parte: ").strip()
                if not patron.isdigit():
                    print("El DNI debe contener sólo números.")
                    continue
                query = "SELECT * FROM personas WHERE dni LIKE ?"
                parametro = f"%{patron}%"
            elif opcion == "2":
                patron = input("Ingresá nombre completo o parte: ").strip()
                if not patron:
                    print("El nombre no puede estar vacío.")
                    continue
                query = "SELECT * FROM personas WHERE nombre LIKE ?"
                parametro = "f%{patron}%"
            else:
                print("Opción inválida.")
                continue

            with sqlite3.connect("mi_base") as conexion:
                cursor = conexion.cursor()
                resultados = cursor.execute(query, (parametro,)).fetchall()
                if resultados:
                    print("\nPersonas encontradas:")
                    for persona in resultados:
                        print(f"DNI: {persona[0]} | NOMBRE: {persona[1]} | EDAD: {persona[2]}")
                else:
                    print("No se encontraron coincidencias")

        except sqlite3.Error as e:
            print(f"Error en la búsqueda de personas (DB): {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")
        
        while True:
            continuar = input("¿Querés hacer otra búsqueda? (S/N): ").strip().lower()
            if continuar == "s":
                break
            elif continuar == "n":
                print("Finalizando búsqueda... ¡Hasta la próxima!")
                return
            else:
                print("Opción inválida. Ingresá S o N:")


 



def menu():
    while True:
        print("\n" + "="*30)
        print("           AGENDA")
        print("="*30)
        print("1. Agregar persona")
        print("2. Buscar persona")
        print("3. Modificar persona")
        print("4. Eliminar persona")
        print("5. Listar todas")
        print("6. Salir")

        try:
            opcion = int(input("Elegí la opción: "))
            match opcion:
                case 1:
                    agregar_persona()
                case 2:
                    buscar_persona()
                case 3:
                    modificar_persona()
                case 4:
                    eliminar_persona()
                case 5:
                    listar_personas()
                case 6:
                    salir()
                    break
                case _:
                    print("Opción inválida")
        except ValueError:
            print("La opción debe ser un número entero")
            continue  

if __name__ == "__main__":
    menu()       