# Enriquecer función buscar_persona_avanzada() incorporando:
# •	✅ Posibilidad de elegir entre AND y OR
# •	✅ Filtro por rango de edad (mínima y/o máxima)
# •	✅ Validaciones claras
# •	✅ Consulta SQL dinámica y segura
# Agregar ordenamiento por nombre, edad y dni y manejo de errores y excepciones.
# Posibilidad e que el usuario haga tantas búsquedas como desee. 
import sqlite3

def buscar_persona_avanzada():
    while True:
        print("\n=== BÚSQUEDA AVANZADA ===")
        condiciones = []
        parametros = []
        # Elección de operador lógico
        modo = input("¿Querés que tu búsqueda sea EXACTA o AMPLIA? (E/A): " ).strip().lower()
        if modo == "e":
            modo = "AND"
        elif modo == "a":
            modo = "OR"
        else: 
            print("Modo de búsqueda Inválido. Se usará 'EXACTA' por defecto.")
            modo = "AND"
        # Filtro por nombre
        nombre = input("Ingresá parte del nombre ( o enter para omitir ): ").strip().lower()
        if nombre:
            condiciones.append("nombre LIKE ?")
            parametros.append(f"%{nombre}%")
        # Filtro por dni
        dni = input("Ingresá parte del DNI ( o enter para omitir ):").strip().lower()
        if dni:
            condiciones.append("dni LIKE ?")
            parametros.append(f"%{dni}%")
        # Filtro por edad exacta
        edad = input("Ingresá la edad exacta ( o enter para omitir )\nSi no sabés la edad exacta, omití y buscá por rangos!"": ").strip()
        if edad:
            if edad.isdigit():
                condiciones.append("edad = ?")
                parametros.append(int(edad))
            else:
                print("La edad debe ser un número.")
                continue
        # Filtro por rango de edad
        edad_min = input("Edad mínima: ").strip()
        edad_max = input("Edad máxima: ").strip()
        if edad_min and edad_max:
            if edad_min.isdigit() and edad_max.isdigit():
                condiciones.append("edad BETWEEN ? AND ?")
                parametros.append(int(edad_min))
                parametros.append(int(edad_max))
            else:
                print("Las edades deben ser números.")
                continue
        elif edad_min:
            if edad_min.isdigit():
                condiciones.append("edad >= ?")
                parametros.append(int(edad_min))
            else:
                print("La edad mínima debe ser un número.")
                continue
        elif edad_max:
            if edad_max.isdigit():
                condiciones.append("edad <= ?")
                parametros.append(int(edad_max))
            else:
                print("La edad máxima debe ser un número.")
                continue
        else:
            print("No ingresaste ningún criterio de búsqueda por edad.")
            continue
        
        print("Filtrando resultados... ¿Cómo los querés ordenados?")
        print("¿Por nombre? ==> Presioná 1")
        print("¿Por DNI? ==> Presioná 2")
        print("¿Por edad? ==> Presioná 3")
        orden = input("Elegí 1, 2 o 3: ").strip()
        if orden and orden.isdigit():
            match orden:
                case "1":
                    orden_sql = " ORDER BY nombre ASC"
                case "2":
                    orden_sql = " ORDER BY dni ASC"
                case "3":
                    orden_sql = " ORDER BY edad ASC"
                case _:
                    print("¡No elegiste 1, 2 o 3! Te los ordeno por nombre.")
                    orden_sql = " ORDER BY nombre ASC"
        else:
            print("¡No elegiste 1, 2 o 3! Te los ordeno por nombre.")
            orden_sql = " ORDER BY nombre ASC"
        # Construcción dinámica de la consulta
        query = "SELECT * FROM personas WHERE " + f" {modo} ".join(condiciones) + orden_sql
        try:
            with sqlite3.connect("mi_base.db") as conexion:
                cursor = conexion.cursor()
                cursor.execute(query, parametros)
                resultados = cursor.fetchall()
                if resultados:
                    print("\nResultados de búsqueda avanzada:")
                    for persona in resultados:
                        print(f"DNI: {persona[0]} | Nombre: {persona[1]} | Edad: {persona[2]}")
                else:
                    print("No se encontraron coincidencias.")
        except sqlite3.Error as e:
            print(f"Error en la búsqueda: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")
        # Preguntar si desea continuar
        while True:
            continua = input("¿Querés realizar otra búsqueda? (S/N): ").strip()
            if continua == "s":
                break
            elif continua == "n":
                print("Finalizando búsqueda avanzada... ¡Hasta la pr+oxima!")
                return
            else:
                print("Respuesta inválida. Ingresá S o N")

if __name__ == "__main__":
    # Solo corre si ejecutás advancedsearch.py directamente
    buscar_persona_avanzada()
