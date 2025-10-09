# 📡 CONNECTION_ISSUES.md  
## 🧠 Registro de problemas técnicos: conexión SQLAlchemy ↔ Supabase  
✍️ Autoría: Ana Sposito  
🗓️ Fecha: Octubre 2025  

---

## 🧩 Problema 1: Error por caracteres especiales en la contraseña

### ❌ Error observado

```python
from sqlalchemy import create_engine
engine = create_engine("postgresql://postgres:MiCl@ve$Segura!@db.xxxxxx.supabase.co:5432/postgres")
```

**Mensaje de error:**

```
sqlalchemy.exc.OperationalError: could not translate host name "Segura!@db.xxxxxx.supabase.co" to address
```

### 🔍 Diagnóstico

La contraseña contiene caracteres especiales (`!`, `@`, `$`) que rompen el formato de la URI. El carácter `@` se interpreta como separador entre contraseña y host, lo que distorsiona el dominio.

### ✅ Solución

Codificar la contraseña usando [URL encoding](https://www.w3schools.com/tags/ref_urlencode.asp):

- `!` → `%21`
- `@` → `%40`
- `$` → `%24`

**URI corregida (con contraseña simulada codificada):**

```python
engine = create_engine("postgresql://postgres:MiCl%40ve%24Segura%21@db.xxxxxx.supabase.co:5432/postgres")
```

> ⚠️ Esta URI está correctamente formada, pero no es compatible con entornos IPv4 como Codespaces. Ver problema 2.

---

## 🧩 Problema 2: Error de red por conexión directa desde entorno IPv4

### ❌ Error observado

Usando la URI corregida del problema 1:

```python
engine = create_engine("postgresql://postgres:MiCl%40ve%24Segura%21@db.xxxxxx.supabase.co:5432/postgres")
```

**Mensaje de error:**

```
sqlalchemy.exc.OperationalError: connection to server at "db.xxxxxx.supabase.co" (...) failed: Network is unreachable
```

### 🔍 Diagnóstico

Supabase ofrece varias URIs de conexión. La **Direct Connection** requiere compatibilidad con IPv6, pero el entorno Codespaces corre sobre IPv4. Por eso no puede alcanzar el host.

### ✅ Solución

Usar la URI **Transaction Pooler**, que es IPv4 compatible:

```python
engine = create_engine("postgresql://postgres.xxxxxx:MiCl%40ve%24Segura%21@aws-1-sa-east-1.pooler.supabase.com:6543/postgres")
```

Esta URI permite conexiones desde entornos como Codespaces, Colab, o máquinas locales con IPv4.

> ✅ Recomendación: guardar la contraseña sin codificar en un archivo `.env` y codificarla en el código usando `quote_plus()` de `urllib.parse`. Ver `SECURITY.md`.

---

## 📘 Versión en inglés (for collaborators or bilingual documentation)

### 🧩 Issue 1: Special characters breaking SQLAlchemy URI

**Error:**
```python
sqlalchemy.exc.OperationalError: could not translate host name "Segura!@db..." to address
```

**Cause:** Unescaped special characters (`!`, `@`, `$`) in the password break URI parsing.

**Fix:** URL-encode the password:
```text
! → %21, @ → %40, $ → %24
```

**Correct URI (with simulated password):**
```python
postgresql://postgres:MiCl%40ve%24Segura%21@db.xxxxxx.supabase.co:5432/postgres
```

> ⚠️ This URI is correctly formed but not compatible with IPv4-only environments like Codespaces.

---

### 🧩 Issue 2: Network unreachable from IPv4-only environment

**Error:**
```text
connection to server at "...supabase.co" failed: Network is unreachable
```

**Cause:** Supabase's Direct Connection requires IPv6. Codespaces uses IPv4.

**Fix:** Use the Transaction Pooler URI (IPv4-compatible):
```python
postgresql://postgres.xxxxxx:MiCl%40ve%24Segura%21@aws-1-sa-east-1.pooler.supabase.com:6543/postgres
```
