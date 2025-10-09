# 📘 README técnico — Limpieza curatorial y exportación a SQLite

## 🧱 Proyecto
Limpieza de datos de clientes y exportación a base SQLite para integración profesional.

## 📂 Fuente
Archivo Excel recibido: `clientes_original_raw.xlsx`

## 🔍 Validaciones aplicadas
- Eliminación de registros con edad menor o igual a 0
- Eliminación de registros con email inválido (sin @, terminados en ".", formato incorrecto)
- Eliminación de registros sin nombre o ciudad
- Eliminación de duplicados

## 📦 Exportación
- Tabla destino: `personas_validas`
- Base de datos: `clientes.db`
- Método: `df.to_sql(..., if_exists="append", index=False)`

##  Versión del script
`validacion_sqlite_v1.0.py`

## Fecha de ejecución
2025-10-08

##  Resultados
- Registros originales: 25
- Registros eliminados por edad inválida: 2
- Registros eliminados por email inválido: 3
- Registros eliminados por nombre o ciudad ausente: 2
- Registros eliminados por duplicados: 0
- Registros exportados: 18

##  Observaciones
Este proceso garantiza trazabilidad curatorial y entrega profesional. Se recomienda incluir este README junto al script y la base exportada.

# 📘 Technical README — Curatorial cleaning and SQLite export

## 🧱 Project
Client data cleaning and export to SQLite database for professional integration.

## 📂 Source
Received Excel file: `clientes_original_raw.xlsx`

## 🔍 Validations applied
- Removed records with age ≤ 0
- Removed records with invalid email (missing @, ending in ".", incorrect format)
- Removed records with missing name or city
- Removed duplicate records

## 📦 Export
- Target table: `personas_validas`
- Database: `clientes.db`
- Method: `df.to_sql(..., if_exists="append", index=False)`

## 🧱 Script version
`validacion_sqlite_v1.0.py`

## 📅 Execution date
2025-10-08

## 📊 Results
- Original records: 25
- Removed due to invalid age: 2
- Removed due to invalid email: 3
- Removed due to missing name or city: 2
- Removed due to duplicates: 0
- Exported records: 18

## 🧭 Notes
This process ensures curatorial traceability and professional delivery. It is recommended to include this README alongside the script and exported database.

