# Entrega curatorial — Clientes Trimestre | TransLog Europa

**Fecha de entrega:** 2025-10-06  
**Versión del script:** `exportador_csv_translog_v1.0.py`  
**Responsable:** Ana Sposito — Analista de datos freelance

## Archivo original recibido
- `clientes_translog_original.csv`
- Ubicación: `data_raw/`
- Contenido: 20 registros, 6 columnas

## Limpieza curatorial aplicada
- Validación de columnas clave: `Nombre`, `Edad`, `Monto`
- Eliminación de nulos y duplicados en esas columnas
- Conversión de tipo: `Edad` → entero

## Exportaciones realizadas

### 1. Exportación intermedia
- Archivo: `clientes_translog_cleaned.csv`
- Ubicación: `data_clean/`
- Contiene todas las columnas originales
- Codificación: `utf-8`

### 2. Exportación curatorial final
- Archivo: `clientes_trimestre.csv`
- Ubicación: `outputs/`
- Columnas incluidas: `Nombre`, `Edad`, `Monto`
- Separador: `;` (compatible con Excel en español)
- Decimal: `,`
- Codificación: `utf-8`

## 🧱 Estructura del proyecto
```plaintext
translogEntrega/
├── data_raw/
│   └── clientes_translog_original.csv
├── data_clean/
│   └── clientes_translog_cleaned.csv
├── outputs/
│   └── clientes_trimestre.csv
├── scripts/
│   └── exportador_csv_translog_v1.0.py
└── docs/
    └── README.md
```

