#  Entrega curatorial — Pacientes Trimestre | SaludDigital LATAM

**Fecha de entrega:** 2025-10-06  
**Versión del script:** `exportador_json_saluddigital_v1.0.py`  
**Responsable:** Ana Sposito — Analista de datos semi-senior

---

##  Archivo original recibido

- `pacientes_saluddigital_original.xlsx`  
- Ubicación: `data_raw/`  
- Contenido: 20 registros, 8 columnas  
- Formato: Excel (.xlsx), codificación UTF-8

---

##  Limpieza curatorial aplicada

- Validación de columnas clave: `Nombre`, `Edad`, `DNI`, `Fecha_turno`, `Especialidad`
- Eliminación de registros con valores nulos en esas columnas
- Eliminación de duplicados sobre esas columnas
- Conversión de tipo: `Edad` → entero (`int`)
- Conservación de acentos y caracteres especiales

---

##  Exportaciones realizadas

### 1. Exportación técnica para integración con API

- Archivo: `pacientes_trimestre.json`  
- Ubicación: `outputs/`  
- Formato: JSON por líneas (`NDJSON`)  
- Parámetros:  
  - `orient="records"`  
  - `lines=True`  
  - `force_ascii=False`  
- Uso previsto: integración directa con base MongoDB

### 2. Exportación legible para revisión humana

- Archivo: `pacientes_trimestre_legible.json`  
- Ubicación: `data_clean/`  
- Formato: JSON estándar tipo array  
- Parámetros:  
  - `orient="records"`  
  - `lines=False`  
  - `indent=4`  
  - `force_ascii=False`  
- Uso previsto: revisión visual, documentación interna

---

##  Estructura del proyecto

```plaintext
saluddigital_entrega/
├── data_raw/
│   └── pacientes_saluddigital_original.xlsx
├── data_clean/
│   └── pacientes_trimestre_legible.json
├── outputs/
│   └── pacientes_trimestre.json
├── scripts/
│   └── exportador_json_saluddigital_v1.0.py
└── docs/
    └── README.md
