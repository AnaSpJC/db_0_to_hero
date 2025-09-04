# Hacer una función que:
# 1.	Pregunta el DNI.
# 2.	Verifica si ya existe en la base.
# 3.	Si existe, muestra un mensaje.
# 4.	Si no, pide nombre y edad, y guarda todo en la tabla.
# 5.    Repite el proceso hasta que el usuario decide finalizar.

import sqlite3

def dni_existe(nombre_db, dni):
    with sqlite3.connect("mi_base.db") as conexion:
        return conexion.execute("SELECT 1 FROM personas WHERE dni= ?", (dni,)).fetchone() is not None
    
def registrar_persona(nombre_db):
    while True:
        dni = input("Qué DNI querés ingresar?: ").strip()
        if dni_existe(nombre_db, dni):
            print("El DNI ya está registrado.")
        else:
            nombre = input("Ingresá el nombre: ").strip()
            edad = input("Ingresá la edad: ").strip()

            with sqlite3.connect("mi_base.db") as conexion:
                cursor = conexion.cursor()
                cursor.execute("INSERT INTO personas VALUES (?, ?, ?)", (dni, nombre, edad))
                print(f"La persona registrada es {nombre} DNI: {dni}, {edad}")
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