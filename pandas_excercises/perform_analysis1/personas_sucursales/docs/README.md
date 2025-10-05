# 📁 Documentación técnica – Encargo Grupo SucursalNet

**Flujo curatorial: limpieza, segmentación y agregación de datos**

---

## 🧼 Fase 2 – Limpieza de nombres y edades  
**Objetivo:** normalizar campos y registrar errores

Se aplicaron funciones con logging para validar y corregir:

- `Nombre`: se eliminaron espacios, se capitalizó y se verificó si era texto alfabético.
- `Edad`: se convirtió a entero y se validó que fuera mayor a cero.

Los errores fueron registrados en columnas técnicas (`Log_nombre`, `Log_edad`) para trazabilidad.  
Los registros inválidos fueron excluidos del archivo limpio.

---

## 🧪 Fase 3 – Derivación de columnas  
**Objetivo:** segmentar por edad

Se generaron columnas derivadas:

- `Mayor`: indica si la persona es mayor de edad (>18).
- `Rango_Etario`: clasifica en "Adolescente", "Jóven", "Adulto", "Mayor".

Estas columnas permiten segmentar la población para análisis interno.

---

## 🧮 Fase 4 – Agregación por sucursal  
**Objetivo:** generar resumen estadístico por sucursal

Se calcularon los siguientes indicadores por sucursal:

- Promedio de edad (`Promedio_Edad`)
- Edad máxima (`Edad_Máxima`)
- Cantidad de personas (`Cantidad_Personas`)

El resultado se exportó como tabla curada para presentación.

---

## 📊 Fase 5 – Ordenamiento  
**Objetivo:** mejorar legibilidad y estética

Se ordenó el archivo limpio por edad descendente.  
Se renumeró el índice para facilitar lectura y presentación.

---

## 📦 Fase 6 – Exportación  
**Objetivo:** generar entregables curados

Se entregaron dos archivos `.xlsx`:

- `personas_limpias.xlsx`: datos limpios, segmentados y ordenados
- `resumen_sucursal.xlsx`: tabla agregada por sucursal

Ambos archivos están listos para presentación interna y análisis.

---

## 📝 Fase 7 – Documentación técnica  
**Objetivo:** garantizar trazabilidad y transparencia

Este documento (`README.md`) resume cada fase del flujo curatorial.  
Se documentaron decisiones técnicas, criterios de exclusión y estructura modular del proyecto.

---

# 🌐 Technical Documentation – SucursalNet Project

**Curatorial workflow: data cleaning, segmentation, and aggregation**

---

## 🧼 Phase 2 – Name and age cleaning  
**Goal:** normalize fields and log errors

Functions with logging were applied to validate and correct:

- `Name`: stripped, capitalized, and checked for alphabetic content.
- `Age`: converted to integer and validated as positive.

Errors were recorded in technical columns (`Log_nombre`, `Log_edad`) for traceability.  
Invalid records were excluded from the clean file.

---

## 🧪 Phase 3 – Column derivation  
**Goal:** age-based segmentation

Derived columns:

- `Mayor`: indicates if the person is over 18.
- `Rango_Etario`: categorizes into "Adolescente", "Jóven", "Adulto", "Mayor".

These columns support internal segmentation and analysis.

---

## 🧮 Phase 4 – Aggregation by branch  
**Goal:** generate statistical summary by branch

Calculated per branch:

- Average age (`Promedio_Edad`)
- Maximum age (`Edad_Máxima`)
- Number of people (`Cantidad_Personas`)

Exported as a curated table for internal use.

---

## 📊 Phase 5 – Sorting  
**Goal:** improve readability and presentation

The clean file was sorted by descending age.  
Index was reset for clarity and aesthetics.

---

## 📦 Phase 6 – Export  
**Goal:** generate curated deliverables

Two `.xlsx` files were delivered:

- `personas_limpias.xlsx`: clean, segmented, and sorted data
- `resumen_sucursal.xlsx`: aggregated table by branch

Both files are ready for internal presentation and analysis.

---

## 📝 Phase 7 – Technical documentation  
**Goal:** ensure traceability and transparency

This document (`README.md`) summarizes each phase of the curatorial workflow.  
Technical decisions, exclusion criteria, and modular structure are documented for internal review.
El flujo curatorial completo está implementado en el script [curatorial_flow_SucursalNet.py](../curatorial_flow_SucursalNet.py)
