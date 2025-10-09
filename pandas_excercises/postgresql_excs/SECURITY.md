# 🔐 SECURITY.md  
## 🧠 Gestión segura de credenciales en proyectos Python  
✍️ Autoría: Ana Sposito  
🗓️ Fecha: Octubre 2025  

---

## ✅ ¿Por qué no incluir contraseñas en el código?

Incluir contraseñas directamente en el código fuente (por ejemplo, en `create_engine()`) es una mala práctica que puede exponer credenciales sensibles si el repositorio se publica o se comparte. Incluso en repositorios privados, es recomendable mantener las claves fuera del código para facilitar la rotación, el versionado y la seguridad.

---

## 🧩 Solución curatorial: uso de `.env` + `python-dotenv` + `.gitignore`

### 📁 Paso 1: Crear archivo `.env`

Ubicación recomendada: en la raíz del proyecto, al mismo nivel que tus carpetas de trabajo.

**Ejemplo de estructura:**
```
/workspaces/db_0_to_hero/pandas_excercises/
├── .env
├── .gitignore
├── postgresql_excs/
│   └── lectura_postgres.py
```

**Contenido del archivo `.env`:**
```env
SUPABASE_PASSWORD=!"##$YOUR_PASSWORD$%&/()=?¡
```

> ⚠️ No codificar la contraseña en `.env`. Se guarda tal como es.

---

### 📁 Paso 2: Crear o editar `.gitignore`

También en la raíz del proyecto. Si no existe, crearlo como:

```
/workspaces/db_0_to_hero/pandas_excercises/.gitignore
```

**Agregar esta línea:**
```gitignore
.env
```

Esto evita que el archivo `.env` se suba al repositorio.

---

### 📦 Paso 3: Instalar `python-dotenv`

Instalar dentro del entorno virtual (`venv`) activo:

```bash
pip install python-dotenv
```

No depende de la carpeta donde estés ubicada, solo del entorno virtual.

---

### 🧪 Paso 4: Leer la contraseña desde Python y codificarla

```python
from sqlalchemy import create_engine
from dotenv import load_dotenv
from urllib.parse import quote_plus
import os

# Cargar variables desde .env
load_dotenv()

# Leer contraseña sin codificar
raw_password = os.getenv("SUPABASE_PASSWORD")

# Codificar para URI
encoded_password = quote_plus(raw_password)

# Construir URI segura
uri = f"postgresql://postgres.wypafronkbgrmsrnthgh:{encoded_password}@aws-1-sa-east-1.pooler.supabase.com:6543/postgres"

# Crear engine
engine = create_engine(uri)
```

---

## 🧠 Notas curadas

- `.env` guarda la contraseña sin codificar.
- `quote_plus()` codifica caracteres especiales para que no rompan la URI.
- Este patrón es seguro, reproducible y profesional.
- Documentar esta práctica en tu README o como archivo separado (`SECURITY.md`) garantiza trazabilidad y buenas prácticas para entornos colaborativos.

## 🛡️ Seguridad de tablas públicas en Supabase  
📅 Octubre 2025  
✍️ Autora: Ana Sposito  

---

### ⚠️ Advertencia detectada

> Supabase alertó que la tabla `public.personas_backup` está expuesta sin políticas de seguridad (RLS no habilitado).

**Mensaje:**
```
Table public.personas_backup is public, but RLS has not been enabled.
```

---

### ✅ Acción curatorial tomada

Se habilitó Row Level Security (RLS) para la tabla `personas_backup` mediante la siguiente instrucción SQL:

```sql
ALTER TABLE public.personas_backup ENABLE ROW LEVEL SECURITY;
```

> Esta acción bloquea el acceso por defecto desde la API REST de Supabase, hasta que se definan políticas explícitas.

---

### 📘 Notas curadas

- La tabla fue creada desde Python usando `to_sql()` como parte del Nivel 2.
- Aunque no se expone desde frontend, se documenta esta acción como parte de las buenas prácticas de seguridad.
- Las políticas específicas de acceso serán definidas en el Nivel 5, durante la simulación completa de cliente real.
- Esta medida garantiza que ningún usuario anónimo pueda acceder a los datos sin autorización.

---

## 🧠 English version (for collaborators)

### ⚠️ Supabase warning

> Table `public.personas_backup` is public, but RLS has not been enabled.

---

### ✅ Curatorial action taken

Row Level Security (RLS) was enabled for the table using:

```sql
ALTER TABLE public.personas_backup ENABLE ROW LEVEL SECURITY;
```

> This blocks all access via Supabase REST API until explicit policies are defined.

---

### 📘 Curated notes

- The table was created via Python using `to_sql()` during Level 2.
- Although not exposed via frontend, this action is documented as part of professional security practices.
- Specific access policies will be defined in Level 5 during the full client simulation.
