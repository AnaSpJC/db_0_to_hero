#  Exportación Excel para integración SQLite
#  Fuente: DataFrame simulado con 25 registros
#  Hoja: 'Personas'
#  Archivo: clientes.xlsx
#  Versión: exportacion_excel_v1.0.py


import pandas as pd

# Datos simulados
data = {
    "Nombre": [
        "Lucía", "Mateo", "Sofía", "Benjamín", "Valentina", "Joaquín", "Martina", "Santiago",
        "Camila", "Tomás", "Agustina", "Francisco", "Julieta", "Lucas", "Mía", "Diego",
        "Isabella", "Gabriel", "Catalina", "Facundo", "Emilia", "Juan", "Renata", "Andrés", "Bianca"
    ],
    "Edad": [
        34, 28, 22, 45, 31, 39, 26, 52, 24, 33, 29, 41, 27, 36, 23, 48, 30, 44, 25, 38, 21, 60, 32, 50, 35
    ],
    "Ciudad": [
        "Buenos Aires", "Córdoba", "Rosario", "Mendoza", "La Plata", "Mar del Plata", "Salta", "Tucumán",
        "San Juan", "Neuquén", "Córdoba", "Buenos Aires", "Rosario", "Mendoza", "La Plata", "Mar del Plata",
        "Salta", "Tucumán", "San Juan", "Neuquén", "Córdoba", "Buenos Aires", "Rosario", "Mendoza", "La Plata"
    ],
    "Email": [
        "lucia@gmail.com", "mateo@yahoo.com", "sofia@hotmail.com", "benjamin@gmail.com", "valentina@yahoo.com",
        "joaquin@hotmail.com", "martina@gmail.com", "santiago@yahoo.com", "camila@hotmail.com", "tomas@gmail.com",
        "agustina@yahoo.com", "francisco@hotmail.com", "julieta@gmail.com", "lucas@yahoo.com", "mia@hotmail.com",
        "diego@gmail.com", "isabella@yahoo.com", "gabriel@hotmail.com", "catalina@gmail.com", "facundo@yahoo.com",
        "emilia@hotmail.com", "juan@gmail.com", "renata@yahoo.com", "andres@hotmail.com", "bianca@gmail.com"
    ]
}

df = pd.DataFrame(data)
df.to_excel("clientes.xlsx", sheet_name="Personas", index=False)

