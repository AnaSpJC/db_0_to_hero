# 🟡 Nivel 2: Conexión desde Python  
✍️ Autoría: Ana Sposito  
🗓️ Fecha: Octubre 2025  

---

## 🎯 Objetivo

Aprender a conectar Python con PostgreSQL usando librerías profesionales, y trabajar con datos desde Pandas de forma segura y reproducible.

---

## 📘 Temas abordados

- `psycopg2`: conexión directa
- `SQLAlchemy`: conexión escalable
- Lectura y escritura con Pandas: `read_sql`, `to_sql`
- Seguridad de claves con `.env` y `quote_plus`
- Documentación curatorial de errores y soluciones

---

## 🧠 Competencias desarrolladas

- Conexión a bases remotas desde entornos IPv4
- Integración entre Python y SQL
- Lectura y exportación curatorial desde Pandas
- Manejo seguro de credenciales
- Documentación técnica reproducible

---

## 🧪 Flujo de conexión con SQLAlchemy

```python
from sqlalchemy import create_engine
from dotenv import load_dotenv
from urllib.parse import quote_plus
import os
import pandas as pd

load_dotenv()
raw_password = os.getenv("SUPABASE_PASSWORD")
encoded_password = quote_plus(raw_password)

uri = f"postgresql://postgres.wypafronkbgrmsrnthgh:{encoded_password}@aws-1-sa-east-1.pooler.supabase.com:6543/postgres"
engine = create_engine(uri)

df = pd.read_sql("SELECT * FROM personas", engine)
df.to_sql("personas_backup", engine, if_exists="replace", index=False)
```

---

## 🔐 Seguridad aplicada

- Contraseña guardada en `.env` sin codificar
- Codificación segura con `quote_plus`
- `.env` protegido por `.gitignore`
- Documentación en `SECURITY.md`

---

## 📎 Documentación complementaria

- [🔐 SECURITY.md](SECURITY.md)
- [📡 CONNECTION_ISSUES.md](CONNECTION_ISSUES.md)

---

## 🧩 Ejemplo adicional: conexión directa con psycopg2

Ver `PSYCOPG_EXAMPLE.md` para implementación alternativa sin SQLAlchemy.
