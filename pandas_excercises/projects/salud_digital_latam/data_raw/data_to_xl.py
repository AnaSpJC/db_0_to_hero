import pandas as pd

# Datos simulados del cliente
data = {
    "Nombre": [
        "Laura Gómez", "Carlos Méndez", "Sofía Ruiz", "Jorge Paredes", "Ana Beltrán",
        "Luis Ortega", "María López", "Federico Torres", "Valentina Díaz", "Pablo Suárez",
        "Lucía Romero", "Martín Herrera", "Camila Vargas", "Diego Ríos", "Elena Navarro",
        "Tomás Aguirre", "Isabel Fuentes", "Ramiro Silva", "Carla Moreno", "Andrés Molina"
    ],
    "Edad": [
        34, 45, 29, 52, 41,
        38, 27, 33, 36, 48,
        31, 40, 26, 50, 43,
        39, 28, 44, 30, 37
    ],
    "DNI": [
        "30123456", "28987654", "31234567", "27876543", "29543210",
        "30456789", "29876543", "31567890", "28765432", "30987654",
        "29654321", "31098765", "29432109", "30876543", "29765432",
        "30543210", "29321098", "31123456", "29210987", "30654321"
    ],
    "Fecha_turno": [
        "2025-07-03", "2025-07-10", "2025-07-15", "2025-07-22", "2025-07-25",
        "2025-08-01", "2025-08-04", "2025-08-10", "2025-08-15", "2025-08-20",
        "2025-08-25", "2025-08-28", "2025-09-01", "2025-09-05", "2025-09-10",
        "2025-09-15", "2025-09-20", "2025-09-25", "2025-09-28", "2025-09-30"
    ],
    "Especialidad": [
        "Cardiología", "Dermatología", "Pediatría", "Neurología", "Ginecología",
        "Oftalmología", "Traumatología", "Endocrinología", "Urología", "Psiquiatría",
        "Otorrinolaringología", "Reumatología", "Gastroenterología", "Oncología", "Nefrología",
        "Neumonología", "Hematología", "Infectología", "Clínica Médica", "Medicina General"
    ],
    "Ciudad": [
        "Buenos Aires", "Córdoba", "Rosario", "Mendoza", "La Plata",
        "Mar del Plata", "San Juan", "Salta", "Tucumán", "Neuquén",
        "Bahía Blanca", "Santa Fe", "Posadas", "San Luis", "Río Gallegos",
        "Formosa", "Resistencia", "Catamarca", "Jujuy", "Paraná"
    ],
    "Teléfono": [
        "11-2345-6789", "351-456-7890", "341-567-8901", "261-678-9012", "221-789-0123",
        "223-890-1234", "264-901-2345", "387-012-3456", "381-123-4567", "299-234-5678",
        "291-345-6789", "342-456-7890", "376-567-8901", "266-678-9012", "2966-789-0123",
        "370-890-1234", "362-901-2345", "383-012-3456", "388-123-4567", "343-234-5678"
    ],
    "Correo": [
        "laura@salud.com", "carlos@salud.com", "sofia@salud.com", "jorge@salud.com", "ana@salud.com",
        "luis@salud.com", "maria@salud.com", "federico@salud.com", "valentina@salud.com", "pablo@salud.com",
        "lucia@salud.com", "martin@salud.com", "camila@salud.com", "diego@salud.com", "elena@salud.com",
        "tomas@salud.com", "isabel@salud.com", "ramiro@salud.com", "carla@salud.com", "andres@salud.com"
    ]
}

df = pd.DataFrame(data)

# Exportar a Excel
df.to_excel("pacientes_saluddigital_original.xlsx", index=False)
