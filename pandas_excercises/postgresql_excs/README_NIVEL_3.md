# 📦 Módulo: validacion_trazabilidad.py  
🧠 Nivel: 3 – Profesional, trazable, exportable  
✍️ Autoría: Ana Sposito  
🗓️ Fecha: Octubre 2025  

## 🇪🇸 Propósito  
Este módulo realiza una validación curatorial de registros simulados, exporta la tabla limpia a Supabase y registra una auditoría técnica en la base de datos. Está diseñado para integrarse con una conexión centralizada (`conexion_supabase.py`) y seguir buenas prácticas de seguridad, trazabilidad y documentación.

## 🇬🇧 Purpose  
This module performs curatorial validation of simulated records, exports the cleaned table to Supabase, and logs a technical audit in the database. It is designed to integrate with a centralized connection (`conexion_supabase.py`) and follow best practices for security, traceability, and documentation.

## 🔍 Validación curatorial  
- Se valida que el campo `email` tenga formato correcto (`@` y `.`).  
- Se descartan registros con `fecha_nacimiento` futura.  
- Se calcula y reporta la cantidad de registros eliminados.

## 📤 Exportación  
- La tabla limpia se exporta como `usuarios_validados` a Supabase.  
- Se utiliza `to_sql()` con `if_exists="replace"` para sobrescribir.

## 🗂 Auditoría técnica  
- Se crea la tabla `log_limpieza` si no existe.  
- Se registra una acción con fecha y descripción.  
- Se utiliza una transacción explícita para garantizar persistencia en Supabase.

## 🔐 Seguridad  
- Las credenciales se cargan desde `.env` usando `dotenv`.  
- La contraseña se codifica con `quote_plus` para evitar errores en la URI.  
- La conexión se centraliza en `conexion_supabase.py` para evitar duplicaciones.

## 🧪 Ejecución  
```bash
python validacion_trazabilidad.py
```

## 📌 Requisitos  
- Python 3.10+  
- Paquetes: `pandas`, `sqlalchemy`, `python-dotenv`  
- Archivo `.env` con variables:  
```dotenv
SUPABASE_USER=postgres.wypafronkbgrmsrnthgh  
SUPABASE_PASSWORD=!t0D4y@g@in$  
SUPABASE_HOST=aws-1-sa-east-1.pooler.supabase.com  
SUPABASE_PORT=6543  
SUPABASE_DB=postgres
```

## 🧠 Notas curatoriales  
- Este módulo forma parte de una suite trazable y exportable para portfolio profesional.  
- La auditoría se registra con persistencia garantizada mediante transacción explícita.  
- La conexión está desacoplada del módulo para facilitar mantenimiento y reutilización.

## 🛡️ Simulación  
Este módulo utiliza datos simulados y credenciales ficticias para fines educativos y curatoriales. No representa una conexión real ni expone datos sensibles.
## 📘 Versión en inglés (for collaborators or bilingual documentation)
# 📦 Module: validacion_trazabilidad.py  
🧠 Level: 3 – Professional, traceable, exportable  
✍️ Author: Ana Sposito  
🗓️ Date: October 2025  

## 🇬🇧 Purpose  
This module performs curatorial validation of simulated records, exports the cleaned table to Supabase, and logs a technical audit in the database. It is designed to integrate with a centralized connection (`conexion_supabase.py`) and follow best practices for security, traceability, and documentation.

## 🔍 Curatorial validation  
- Validates that the `email` field has a proper format (`@` and `.`).  
- Discards records with future `fecha_nacimiento` (birth dates).  
- Calculates and reports the number of records removed.

## 📤 Export  
- The cleaned table is exported to Supabase as `usuarios_validados`.  
- Uses `to_sql()` with `if_exists="replace"` to overwrite previous data.

## 🗂 Technical audit  
- Creates the `log_limpieza` table if it doesn't exist.  
- Logs an action with timestamp and description.  
- Uses an explicit transaction to ensure persistence in Supabase.

## 🔐 Security  
- Credentials are loaded from `.env` using `dotenv`.  
- Password is encoded with `quote_plus` to avoid URI errors.  
- Connection is centralized in `conexion_supabase.py` to avoid duplication.

## 🧪 Execution  
```bash
python validacion_trazabilidad.py
```

## 📌 Requirements  
- Python 3.10+  
- Packages: `pandas`, `sqlalchemy`, `python-dotenv`  
- `.env` file with variables:  
```dotenv
SUPABASE_USER=postgres.wypafronkbgrmsrnthgh  
SUPABASE_PASSWORD=!t0D4y@g@in$  
SUPABASE_HOST=aws-1-sa-east-1.pooler.supabase.com  
SUPABASE_PORT=6543  
SUPABASE_DB=postgres
```

## 🧠 Curatorial notes  
- This module is part of a traceable and exportable suite for professional portfolio use.  
- Audit logs are recorded with guaranteed persistence via explicit transaction.  
- Connection logic is decoupled from the module to support maintainability and reuse.

## 🛡️ Simulation  
This module uses simulated data and fictitious credentials for educational and curatorial purposes. It does not represent a real connection or expose sensitive information.
