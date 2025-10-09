# 🔗 PSYCOPG_EXAMPLE.md  
## 🧪 Conexión directa a Supabase con psycopg2  
✍️ Autoría: Ana Sposito  
🗓️ Fecha: Octubre 2025  

---

## 🎯 Propósito

Explorar la conexión directa a PostgreSQL desde Python usando `psycopg2`, sin usar SQLAlchemy. Este enfoque permite entender el manejo de parámetros explícitos y el uso de `read_sql` con Pandas.

---

## 📦 Requisitos

- psycopg2 instalado en el entorno virtual
- `.env` con contraseña simulada
- `.gitignore` protegiendo `.env`

---

## 🧪 Ejemplo completo

```python
import psycopg2
import os
from dotenv import load_dotenv
import pandas as pd

# 🔐 Cargar contraseña desde .env
load_dotenv()
password = os.getenv("SUPABASE_PASSWORD")

# 🔗 Conexión directa
conn = psycopg2.connect(
    host="aws-1-sa-east-1.pooler.supabase.com",
    database="postgres",
    user="postgres.wypafronkbgrmsrnthgh",
    password=password,
    port=6543
)

# 📥 Lectura curatorial
df = pd.read_sql("SELECT * FROM personas", conn)
print(df.head())
```

---

## ⚠️ Limitaciones

- `to_sql()` no funciona con `psycopg2` directamente.
- Para exportar, se recomienda usar SQLAlchemy o escribir manualmente con `cursor.execute()`.

---

## 🧠 Notas curadas

Este ejemplo complementa el enfoque escalable de SQLAlchemy y permite comparar estilos de conexión, manejo de errores y compatibilidad con Pandas.

