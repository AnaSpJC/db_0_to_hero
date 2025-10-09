"""
📦 Módulo: lectura_postgres.py  
🧠 Propósito: Conexión segura a Supabase desde Python usando SQLAlchemy  
✍️ Autoría: Ana Sposito  
🗓️ Fecha: Octubre 2025  
"""

# 🔐 Seguridad: carga de credenciales desde archivo .env
from dotenv import load_dotenv
from urllib.parse import quote_plus
import os

load_dotenv()
raw_password = os.getenv("SUPABASE_PASSWORD")
encoded_password = quote_plus(raw_password)

# 🔗 Conexión escalable con SQLAlchemy
from sqlalchemy import create_engine
import pandas as pd

uri = f"postgresql://postgres.wypafronkbgrmsrnthgh:{encoded_password}@aws-1-sa-east-1.pooler.supabase.com:6543/postgres"
engine = create_engine(uri)

# 📥 Lectura curatorial desde Supabase
df = pd.read_sql("SELECT * FROM personas", engine)
print(df.head())

# 📤 Exportación curatorial a tabla backup
df.to_sql("personas_backup", engine, if_exists="replace", index=False)
