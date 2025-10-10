"""
📦 Módulo: conexion_supabase.py  
🧠 Propósito: Conexión segura y centralizada a Supabase usando SQLAlchemy  
✍️ Autoría: Ana Sposito  
🗓️ Fecha: Octubre 2025  
"""

# 🔐 Seguridad: carga de credenciales desde archivo .env
from dotenv import load_dotenv
from urllib.parse import quote_plus
import os
from sqlalchemy import create_engine

# Cargar variables desde .env
load_dotenv()
user = os.getenv("SUPABASE_USER")
raw_password = os.getenv("SUPABASE_PASSWORD")
encoded_password = quote_plus(raw_password)
host = os.getenv("SUPABASE_HOST")
port = os.getenv("SUPABASE_PORT")
db = os.getenv("SUPABASE_DB")

# Construir URI segura
uri = f"postgresql://{user}:{encoded_password}@{host}:{port}/{db}"

# Crear motor de conexión
engine = create_engine(uri)
