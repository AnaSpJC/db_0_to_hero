# 📦 Formatos JSON utilizados en la entrega | SaludDigital LATAM

Este documento complementa el README técnico y explica las diferencias entre los formatos JSON entregados, su propósito curatorial y su uso previsto por el cliente.

---

## 🔹 JSON por líneas (`NDJSON`)

**Archivo entregado:** `pacientes_trimestre.json`  
**Ubicación:** `outputs/`  
**Generado con:**

```python
df.to_json("pacientes_trimestre.json", orient="records", lines=True, force_ascii=False)
```

### Características técnicas

- Cada línea representa un objeto JSON independiente  
- No está envuelto en corchetes `[]`  
- No tiene comas entre objetos  
- Compatible con bases NoSQL como MongoDB  
- Ideal para integración con APIs que procesan datos por streaming o lote

### Ventajas curatorialmente relevantes

- Alta eficiencia en lectura por sistemas  
- Permite procesamiento incremental  
- Evita errores de formato en sistemas que no aceptan arrays JSON

## 🔹 JSON legible tipo array

**Archivo entregado:** `pacientes_trimestre_legible.json`  
**Ubicación:** `data_clean/`  
**Generado con:**

```python
df.to_json("pacientes_trimestre_array.json", orient="records", lines=False, force_ascii=False, indent=4)
```


### 🧪 Características técnicas

- Todo el contenido está dentro de un array `[]`  
- Cada objeto tiene sangría (`indent=4`) y salto de línea  
- Compatible con editores visuales, validadores JSON y revisión humana

### 🧱 Ventajas curatorialmente relevantes

- Facilita la lectura y validación manual  
- Útil para documentación interna o revisión por equipos no técnicos  
- Permite detectar errores de contenido antes de integración
### 🧭 Recomendación curatorial

Se entregan ambos formatos para cubrir dos necesidades complementarias:

| Formato                  | Uso técnico                      | Uso documental                     |
|--------------------------|----------------------------------|------------------------------------|
| NDJSON (`lines=True`)    | Integración con MongoDB, APIs    | No apto para validadores visuales  |
| JSON legible (`indent=4`)| Revisión humana, documentación   | No apto para procesamiento por lotes |

### Versión del documento

- **Archivo:** `formato_json_curatorial.md`  
- **Fecha:** 2025-10-06  
- **Complementa:** `README.md` y `exportador_json_saluddigital_v1.0.py`  
- **Responsable:** Ana Sposito — Analista de datos semi-senior

