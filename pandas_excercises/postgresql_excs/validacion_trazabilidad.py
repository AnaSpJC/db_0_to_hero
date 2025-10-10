"""
📦 Módulo: validacion_trazabilidad.py  
🧠 Propósito: Validación curatorial de registros y exportación segura a Supabase  
✍️ Autoría: Ana Sposito  
🗓️ Fecha: Octubre 2025  
"""

# ──📦 Imports
import pandas as pd
from datetime import datetime
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from conexion_supabase import engine  # 🔗 Conexión centralizada

# ──📊 Simulación de datos
df = pd.DataFrame({
    "email": ["ana@mail.com", None, "malformado@", "lucas@dominio.com"],
    "fecha_nacimiento": ["1990-05-12", "2025-01-01", "1985-07-30", "2000-12-01"],
    "pais": ["AR", "AR", "BR", "AR"]
})

# ──🔍 Función de validación curatorial
def email_valido(email):
    return isinstance(email, str) and "@" in email and "." in email.split("@")[-1]

df_validado = df[
    df["email"].apply(email_valido) &
    (pd.to_datetime(df["fecha_nacimiento"], errors="coerce") < datetime.today())
]

# ──📋 Log técnico
registros_eliminados = len(df) - len(df_validado)
print(f"🔍 Se eliminaron {registros_eliminados} registros por validación curatorial.")

# ──📤 Exportar tabla limpia a Supabase
df_validado.to_sql(
    name="usuarios_validados",
    con=engine,
    if_exists="replace",
    index=False
)
print("✅ Tabla limpia exportada correctamente.")

# ──🗂 Auditoría en base: crear tabla si no existe y registrar acción
try:
    
    with engine.begin() as conn:  # ✅ begin() garantiza commit automático
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS log_limpieza (
                id SERIAL PRIMARY KEY,
                fecha TIMESTAMP,
                accion TEXT
            )
        """))
        accion = f"Eliminados {registros_eliminados} registros inválidos"
        fecha = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        conn.execute(text("""
            INSERT INTO log_limpieza (fecha, accion)
            VALUES (:fecha, :accion)
        """), {"fecha": fecha, "accion": accion})
    print("📝 Auditoría registrada en log_limpieza.")
except SQLAlchemyError as e:
    print(f"❌ Error al crear/insertar en log_limpieza: {e}")
