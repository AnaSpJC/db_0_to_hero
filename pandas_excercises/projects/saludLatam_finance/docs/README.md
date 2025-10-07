# Informe Curatorial: Finanzas Clínicas LATAM

## 🧾 Caso
**Cliente:** Dirección de Finanzas de una red de clínicas privadas  
**Consultora:** SaludDigital LATAM  
**Fecha:** Octubre 2025  
**Responsable técnica:** Ana Sposito

## 🎯 Objetivo
Generar un archivo Excel con dos hojas:
- **Resumen mensual de pacientes** ingresados entre julio y septiembre 2025
- **Detalle de montos facturados por edad**, agrupado y validado

## 🛠️ Flujo curatorial
1. **Carga del archivo original** desde `/data_raw`
2. **Limpieza curatorial**: duplicados, nulos, tipos (`float`, `datetime`)
3. **Validación estructural**: sin nulos, columnas consistentes
4. **Generación de hoja resumen** con columna `Mes_Ingreso` y fechas en formato `dd/mm/yyyy`
5. **Generación de hoja de montos por edad** con totales y cantidad de pacientes
6. **Exportación profesional** con `XlsxWriter`:
   - Encabezados en negrita
   - Texto centrado
   - Columnas ajustadas
   - Formato de fecha LATAM

## 📦 Entregables
- `informe_finanzas_octubre2025.xlsx`  
  - Hoja 1: `Resumen_Pacientes`  
  - Hoja 2: `Montos_por_Edad`
- `resumen_intermedio.csv` (estado previo para revisión)

## 📁 Estructura de carpetas

```text
projects/saludLatam_finance/
├── data_raw/
│   └── pacientes_julio-sep2025.csv
├── data_clean/
│   └── resumen_intermedio.csv
├── outputs/
│   └── informe_finanzas_octubre2025.xlsx
├── script/
│   └── procesamiento_finanzas.py
└── README.md
```
## 🔐 Validaciones aplicadas

- Sin nulos ni duplicados  
- Tipos consistentes (`float`, `str`, `datetime`)  
- Columnas claras para revisión contable

## 🧠 Observaciones

Este flujo está diseñado para ser reproducible, auditable y adaptable a nuevos períodos.  
Puede integrarse fácilmente a pipelines de exportación mensual o dashboards financieros.
